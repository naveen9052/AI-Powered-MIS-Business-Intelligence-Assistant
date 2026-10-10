from app.services.report_service import get_summary


def allowed_tools() -> dict:
    """Python functions that the AI is allowed to call."""
    return {
        "get_summary": get_summary
    }


def tool_declarations() -> list[dict]:
    """Function declarations sent to Gemini."""

    return [
        {
            "type": "function",
            "name": "get_summary",
            "description": (
                "Get the current MIS business summary including "
                "active employee count, present employees, "
                "monthly sales, and attendance rate."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
            },
        }
    ]