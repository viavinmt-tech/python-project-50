from gendiff.parser import parse_file
from gendiff.diff_builder import build_diff
from gendiff.formatters.stylish import format_stylish


def generate_diff(filepath1: str, filepath2: str, format_name: str = 'stylish') -> str:

    data1 = parse_file(filepath1)
    data2 = parse_file(filepath2)
    
    diff = build_diff(data1, data2)
    
    if format_name == 'stylish':
        return format_stylish(diff)
    else:
        raise ValueError(f"Unknown format: {format_name}")