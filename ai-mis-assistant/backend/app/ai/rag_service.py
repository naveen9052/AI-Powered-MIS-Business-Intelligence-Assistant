from pathlib import Path
from app.config.settings import PROJECT_ROOT


def search_policies(query: str) -> list[dict[str, str]]:
    """Search text policy files; PDF/vector indexing can be added later."""
    matches = []
    for path in (PROJECT_ROOT / "documents").glob("*.txt"):
        content = path.read_text(encoding="utf-8", errors="ignore")
        if query.casefold() in content.casefold():
            matches.append({"source": path.name, "excerpt": content[:500]})
    return matches
