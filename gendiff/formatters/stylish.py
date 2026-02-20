import json
from typing import Any, Dict, List


def _format_value(value: Any, depth: int) -> str:
    indent = "    " * depth

    if isinstance(value, dict):
        lines = ["{"]
        for k, v in value.items():
            lines.append(f"{indent}    {k}: {_format_value(v, depth + 1)}")
        lines.append(indent + "}")
        return "\n".join(lines)
    elif isinstance(value, str):
        return value
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return json.dumps(value)


def _format_line(prefix: str, key: str, value: Any, sign_indent: str, depth: int) -> str:
    formatted = _format_value(value, depth)
    if formatted == "":
        return f"{sign_indent}{prefix} {key}: "
    return f"{sign_indent}{prefix} {key}: {formatted}"


def _iter_node(node: Dict[str, Any], depth: int) -> List[str]:
    indent = "    " * (depth - 1)
    sign_indent = indent + "  "
    lines = []
    node_type = node["type"]
    key = node["key"]

    if node_type == "nested":
        lines.append(f"{indent}    {key}: {{")
        for child in node.get("children", []):
            lines.extend(_iter_node(child, depth + 1))
        lines.append(f"{indent}    }}")

    elif node_type == "added":
        lines.append(_format_line("+", key, node["value"], sign_indent, depth))

    elif node_type == "removed":
        lines.append(_format_line("-", key, node["value"], sign_indent, depth))

    elif node_type == "unchanged":
        value = _format_value(node["value"], depth)
        if value == "":
            lines.append(f"{indent}    {key}: ")
        else:
            lines.append(f"{indent}    {key}: {value}")

    elif node_type == "changed":
        lines.append(_format_line("-", key, node["old_value"], sign_indent, depth))
        lines.append(_format_line("+", key, node["new_value"], sign_indent, depth))

    return lines


def format_stylish(diff: List[Dict[str, Any]]) -> str:
    lines = ["{"]

    for node in diff:
        lines.extend(_iter_node(node, 1))

    lines.append("}")
    return "\n".join(lines)
