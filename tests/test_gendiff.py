import os
import pytest
from gendiff import generate_diff


def get_fixture_path(filename):
    
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'fixtures', filename)


def read_file(path):

    with open(path, 'r') as f:
        return f.read().rstrip()


@pytest.mark.parametrize('file1,file2,format_name,expected', [
    ('file1.json', 'file2.json', 'stylish', 'expected_result.txt'),
    ('file1.yml', 'file2.yml', 'stylish', 'expected_result.txt'),
    
    ('file1_nested.json', 'file2_nested.json', 'stylish', 'expected_nested.txt'),
    ('file1_nested.yml', 'file2_nested.yml', 'stylish', 'expected_nested.txt'),
    
    ('file1_nested.json', 'file2_nested.json', 'plain', 'expected_plain.txt'),
    ('file1_nested.yml', 'file2_nested.yml', 'plain', 'expected_plain.txt'),
])
def test_generate_diff(file1, file2, format_name, expected):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_path = get_fixture_path(expected)
    
    result = generate_diff(file1_path, file2_path, format_name)
    expected_result = read_file(expected_path)
    
    assert result == expected_result


def test_generate_diff_with_identical_files():

    file1 = get_fixture_path('file1_nested.json')
    
    for format_name in ['stylish', 'plain']:
        result = generate_diff(file1, file1, format_name)
        
        if format_name == 'stylish':
            assert result
        else: 
            assert result == ''


def test_generate_diff_mixed_formats():
    json_file = get_fixture_path('file1_nested.json')
    yaml_file = get_fixture_path('file2_nested.yml')
    expected_path = get_fixture_path('expected_plain.txt')
    
    result = generate_diff(json_file, yaml_file, 'plain')
    expected_result = read_file(expected_path)
    
    assert result == expected_result


def test_generate_diff_invalid_format():
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    
    with pytest.raises(ValueError, match="Unknown format: invalid"):
        generate_diff(file1, file2, 'invalid')


@pytest.mark.parametrize('format_name', ['stylish', 'plain'])
def test_generate_diff_format_choices(format_name):
    file1 = get_fixture_path('file1.json')
    file2 = get_fixture_path('file2.json')
    
    result = generate_diff(file1, file2, format_name)
    assert isinstance(result, str)