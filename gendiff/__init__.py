from gendiff.parser import parse_file


def generate_diff(filepath1: str, filepath2: str) -> str:
    
    data1 = parse_file(filepath1)
    data2 = parse_file(filepath2)


    
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    lines = []
    
    for key in all_keys:
        if key not in data2:
            lines.append(f"  - {key}: {data1[key]}")
        elif key not in data1:
            lines.append(f"  + {key}: {data2[key]}")
        elif data1[key] == data2[key]:
            lines.append(f"    {key}: {data1[key]}")
        else:
            lines.append(f"  - {key}: {data1[key]}")
            lines.append(f"  + {key}: {data2[key]}")
    
    return '{\n' + '\n'.join(lines) + '\n}'

