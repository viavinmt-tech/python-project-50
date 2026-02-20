import json
from typing import Any, Dict, List


def format_json(diff: List[Dict[str, Any]]) -> str:

    return json.dumps(diff, indent=2, ensure_ascii=False)
