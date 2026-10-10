import json
import os

from dotenv import load_dotenv
from google import genai

from app.ai.tools import allowed_tools, tool_declarations


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY is not configured.")

client = genai.Client(api_key=GEMINI_API_KEY)


def answer_question(question: str) -> str:
    """Answer MIS questions using Gemini and approved business tools."""

    interaction = client.interactions.create(
        model="gemini-3.5-flash",
        input=(
            "You are an AI assistant for an internal business MIS system. "
            "For questions about current MIS business data, use the available "
            "business tools instead of guessing. "
            "Explain the returned data clearly and professionally.\n\n"
            f"User question: {question}"
        ),
        tools=tool_declarations(),
    )

    available_functions = allowed_tools()
    function_results = []

    for step in interaction.steps:
        if step.type == "function_call":
            function = available_functions.get(step.name)

            if function is None:
                continue

            result = function(**step.arguments)

            function_results.append({
                "type": "function_result",
                "name": step.name,
                "call_id": step.id,
                "result": [
                    {
                        "type": "text",
                        "text": json.dumps(result, default=str)
                    }
                ]
            })

    if not function_results:
        return interaction.output_text

    final_interaction = client.interactions.create(
        model="gemini-3.5-flash",
        previous_interaction_id=interaction.id,
        input=function_results,
        tools=tool_declarations(),
    )

    return final_interaction.output_text