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
        prefix = "+"
        value = _format_value(node["value"], depth)
        if value == "":
            lines.append(f"{sign_indent}{prefix} {key}:")
        else:
            lines.append(f"{sign_indent}{prefix} {key}: {value}")

    elif node_type == "removed":
        prefix = "-"
        value = _format_value(node["value"], depth)
        if value == "":
            lines.append(f"{sign_indent}{prefix} {key}: ")
        else:
            lines.append(f"{sign_indent}{prefix} {key}: {value}")

    elif node_type == "unchanged":
        value = _format_value(node["value"], depth)
        if value == "":
            lines.append(f"{indent}    {key}:")
        else:
            lines.append(f"{indent}    {key}: {value}")

    elif node_type == "changed":
        old_value = _format_value(node["old_value"], depth)
        new_value = _format_value(node["new_value"], depth)

        if old_value == "":
            lines.append(f"{sign_indent}- {key}: ")
        else:
            lines.append(f"{sign_indent}- {key}: {old_value}")

        if new_value == "":
            lines.append(f"{sign_indent}+ {key}:")
        else:
            lines.append(f"{sign_indent}+ {key}: {new_value}")

    return lines


def format_stylish(diff: List[Dict[str, Any]]) -> str:
    lines = ["{"]

    for node in diff:
        lines.extend(_iter_node(node, 1))

    lines.append("}")
    return "\n".join(lines)
