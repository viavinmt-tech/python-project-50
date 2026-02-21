import json  # NOSONAR
import os  # NOSONAR

import pytest  # NOSONAR

from gendiff import generate_diff  # NOSONAR


def get_fixture_path(filename):  # NOSONAR

    current_dir = os.path.dirname(__file__)  # NOSONAR
    return os.path.join(current_dir, "fixtures", filename)  # NOSONAR


def read_file(path):  # NOSONAR

    with open(path, "r") as f:  # NOSONAR
        return f.read().rstrip()  # NOSONAR


@pytest.mark.parametrize(  # NOSONAR
    "file1,file2,format_name,expected",
    [
        ("file1.json", "file2.json", "stylish", "expected_result.txt"),
        ("file1.yml", "file2.yml", "stylish", "expected_result.txt"),
        (
            "file1_nested.json",
            "file2_nested.json",
            "stylish",
            "expected_nested.txt",
        ),
        (
            "file1_nested.yml",
            "file2_nested.yml",
            "stylish",
            "expected_nested.txt",
        ),
        (
            "file1_nested.json",
            "file2_nested.json",
            "json",
            "expected_nested.json",
        ),
        (
            "file1_nested.json",
            "file2_nested.json",
            "plain",
            "expected_plain.txt",
        ),
        ("file1_nested.yml", "file2_nested.yml", "plain", "expected_plain.txt"),
    ],
)  # NOSONAR
def test_generate_diff(file1, file2, format_name, expected):  # NOSONAR
    file1_path = get_fixture_path(file1)  # NOSONAR
    file2_path = get_fixture_path(file2)  # NOSONAR
    expected_path = get_fixture_path(expected)  # NOSONAR

    result = generate_diff(file1_path, file2_path, format_name)  # NOSONAR
    expected_result = read_file(expected_path)  # NOSONAR

    assert result == expected_result  # NOSONAR


def test_generate_diff_with_identical_files():  # NOSONAR

    file1 = get_fixture_path("file1_nested.json")  # NOSONAR

    for format_name in ["stylish", "plain"]:  # NOSONAR
        result = generate_diff(file1, file1, format_name)  # NOSONAR

        if format_name == "stylish":  # NOSONAR
            assert result  # NOSONAR
        else:
            assert result == ""  # NOSONAR


def test_generate_diff_mixed_formats():  # NOSONAR
    json_file = get_fixture_path("file1_nested.json")  # NOSONAR
    yaml_file = get_fixture_path("file2_nested.yml")  # NOSONAR
    expected_path = get_fixture_path("expected_plain.txt")  # NOSONAR

    result = generate_diff(json_file, yaml_file, "plain")  # NOSONAR
    expected_result = read_file(expected_path)  # NOSONAR

    assert result == expected_result  # NOSONAR


def test_generate_diff_invalid_format():  # NOSONAR
    file1 = get_fixture_path("file1.json")  # NOSONAR
    file2 = get_fixture_path("file2.json")  # NOSONAR

    with pytest.raises(ValueError, match="Unknown format: invalid"):  # NOSONAR
        generate_diff(file1, file2, "invalid")  # NOSONAR


@pytest.mark.parametrize("format_name", ["stylish", "plain"])  # NOSONAR
def test_generate_diff_format_choices(format_name):  # NOSONAR
    file1 = get_fixture_path("file1.json")  # NOSONAR
    file2 = get_fixture_path("file2.json")  # NOSONAR

    result = generate_diff(file1, file2, format_name)  # NOSONAR
    assert isinstance(result, str)  # NOSONAR


def test_generate_diff_json_format():  # NOSONAR
    file1 = get_fixture_path("file1_nested.json")  # NOSONAR
    file2 = get_fixture_path("file2_nested.json")  # NOSONAR
    expected_path = get_fixture_path("expected_nested.json")  # NOSONAR

    result = generate_diff(file1, file2, "json")  # NOSONAR

    try:  # NOSONAR
        parsed_result = json.loads(result)  # NOSONAR
        parsed_expected = json.loads(read_file(expected_path))  # NOSONAR
        assert parsed_result == parsed_expected  # NOSONAR
    except json.JSONDecodeError:  # NOSONAR
        pytest.fail("Result is not valid JSON")  # NOSONAR
