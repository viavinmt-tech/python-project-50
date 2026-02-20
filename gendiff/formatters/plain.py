from typing import Any, Dict, List


def _stringify(value: Any) -> str:
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (int, float)):
        return str(value)
    else:
        return str(value)


def _iter_node(node: Dict[str, Any], path: str = "") -> List[str]:
    lines = []
    current_path = f"{path}.{node['key']}" if path else node["key"]

    node_type = node["type"]

    if node_type == "nested":
        for child in node.get("children", []):
            lines.extend(_iter_node(child, current_path))

    elif node_type == "added":
        value = _stringify(node["value"])
        lines.append(f"Property '{current_path}' was added with value: {value}")

    elif node_type == "removed":
        lines.append(f"Property '{current_path}' was removed")

    elif node_type == "changed":
        old_value = _stringify(node["old_value"])
        new_value = _stringify(node["new_value"])
        lines.append(
            f"Property '{current_path}' was updated. "
            f"From {old_value} to {new_value}"
        )

    return lines


def format_plain(diff: List[Dict[str, Any]]) -> str:
    lines = []
    for node in diff:
        lines.extend(_iter_node(node))

    return "\n".join(lines)
