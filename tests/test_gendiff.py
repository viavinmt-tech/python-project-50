import os
import pytest
from gendiff import generate_diff


def get_fixture_path(filename):
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', filename)


def read_file(path):
    with open(path, 'r') as f:
        return f.read().strip()


def test_generate_diff():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = get_fixture_path('expected_result.txt')
    
    result = generate_diff(file1, file2)
    expected_result = read_file(expected)
    
    assert result == expected_result


def test_generate_diff_with_identical_files():
    file1 = get_fixture_path('file1.json')
    
    result = generate_diff(file1, file1)
    
    lines = result.strip().split('\n')
    assert all(line.startswith('    ') for line in lines[1:-1] if ':' in line)


def test_generate_diff_cli():
    import subprocess
    
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    expected = get_fixture_path('expected_result.txt')
    
    result = subprocess.run(
        ['gendiff', file1, file2],
        capture_output=True,
        text=True
    )
    
    expected_result = read_file(expected)
    assert result.stdout.strip() == expected_result
    assert result.returncode == 0


def test_generate_diff_help():
    import subprocess
    
    result = subprocess.run(
        ['gendiff', '--help'],
        capture_output=True,
        text=True
    )
    
    assert 'usage:' in result.stdout
    assert 'Compares two configuration files' in result.stdout
    assert result.returncode == 0


@pytest.mark.parametrize('file1,file2,expected', [
    ('file1.json', 'file2.json', 'expected_result.txt'),
])
def test_generate_diff_parametrized(file1, file2, expected):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_path = get_fixture_path(expected)
    
    result = generate_diff(file1_path, file2_path)
    expected_result = read_file(expected_path)
    
    assert result == expected_result
