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
        return f.read().rstrip()


@pytest.mark.parametrize('file1,file2,expected', [
    # Плоские файлы
    ('file1.json', 'file2.json', 'expected_result.txt'),
    ('file1.yml', 'file2.yml', 'expected_result.txt'),
    ('file1.yaml', 'file2.yaml', 'expected_result.txt'),
    # Вложенные файлы
    ('file1_nested.json', 'file2_nested.json', 'expected_nested.txt'),
    ('file1_nested.yml', 'file2_nested.yml', 'expected_nested.txt'),
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
    file1 = get_fixture_path('file1_nested.json')
    
    result = generate_diff(file1, file1)
    lines = result.strip().split('\n')
    
    # Проверяем, что нет знаков + или -
    for line in lines:
        if ':' in line and not line.strip().startswith('{') and not line.strip().startswith('}'):
            assert line.strip()[0] == ' '


def test_generate_diff_mixed_formats():
    """Test diff between JSON and YAML files."""
    json_file = get_fixture_path('file1_nested.json')
    yaml_file = get_fixture_path('file2_nested.yml')
    expected_path = get_fixture_path('expected_nested.txt')
    
    result = generate_diff(json_file, yaml_file)
    expected_result = read_file(expected_path)
    
    assert result == expected_result


def test_generate_diff_unsupported_format():
    """Test error with unsupported file format."""
    with pytest.raises(ValueError):
        generate_diff('file1.txt', 'file2.txt')


@pytest.mark.parametrize('format_name', ['stylish', 'unknown'])
def test_generate_diff_format(format_name):
    """Test different output formats."""
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    
    if format_name == 'unknown':
        with pytest.raises(ValueError):
            generate_diff(file1, file2, format_name)
    else:
        result = generate_diff(file1, file2, format_name)
        assert isinstance(result, str)
        assert len(result) > 0