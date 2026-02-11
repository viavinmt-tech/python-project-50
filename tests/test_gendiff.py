import os
import pytest
from gendiff import generate_diff


def get_fixture_path(filename):
    """Get absolute path to fixture file."""
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', filename)


def read_file(path):
    """Read file content."""
    with open(path, 'r') as f:
        return f.read().strip()





@pytest.mark.parametrize('file1,file2,expected', [
    ('file1.json', 'file2.json', 'expected_result.txt'),
    ('file1.yml', 'file2.yml', 'expected_result.txt'),
    ('file1.yaml', 'file2.yaml', 'expected_result.txt'),
])
def test_generate_diff(file1, file2, expected):
    """Test diff generation for different file formats."""
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_path = get_fixture_path(expected)
    
    result = generate_diff(file1_path, file2_path)
    expected_result = read_file(expected_path)
    
    assert result == expected_result


def test_generate_diff_with_identical_files():
    """Test diff with identical files."""
    file1 = get_fixture_path('file1.json')
    
    result = generate_diff(file1, file1)
    lines = result.strip().split('\n')
    assert all(line.startswith('    ') for line in lines[1:-1] if ':' in line)


def test_generate_diff_mixed_formats():
    """Test diff between JSON and YAML files."""
    json_file = get_fixture_path('file1.json')
    yaml_file = get_fixture_path('file2.yml')
    expected_path = get_fixture_path('expected_result.txt')
    
    result = generate_diff(json_file, yaml_file)
    expected_result = read_file(expected_path)
    
    assert result == expected_result


def test_generate_diff_unsupported_format():
    """Test error with unsupported file format."""
    with pytest.raises(ValueError, match="Unsupported file format"):
        generate_diff('file1.txt', 'file2.txt')


@pytest.mark.parametrize('extension', ['yml', 'yaml'])
def test_yaml_extensions(extension):
    """Test both .yml and .yaml extensions."""
    file1 = get_fixture_path(f'file1.{extension}')
    file2 = get_fixture_path(f'file2.{extension}')
    expected_path = get_fixture_path('expected_result.txt')
    
    result = generate_diff(file1, file2)
    expected_result = read_file(expected_path)
    
    assert result == expected_result