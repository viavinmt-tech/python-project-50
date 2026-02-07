import json


def generate_diff(filepath1: str, filepath2: str) -> str:
    
    def read_file(path: str) -> dict:
        with open(path, 'r') as f:
            return json.load(f)
    
    data1 = read_file(filepath1)
    data2 = read_file(filepath2)
    
    # Build diff
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
