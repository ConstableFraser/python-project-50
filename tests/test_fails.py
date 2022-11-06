import pytest
import json
from gendiff.generate_diff import generate_diff


@pytest.fixture
def correct_json():
    file1 = "tests/fixtures/json/json1.json"
    file2 = "tests/fixtures/json/json2.json"
    return file1, file2


@pytest.fixture
def correct_result():
    result = "tests/fixtures/result.txt"
    return result


def test_fail_file(correct_json,correct_result):
    filename1, filename2 = correct_json
    f = open(correct_result)
    result = f.readlines()
    f.close
    assert "".join(result) != generate_diff(filename1, "filefail0295892.json")


def test_fail_format(correct_json,correct_result):
    filename1, filename2 = correct_json
    f = open(correct_result)
    result = f.readlines()
    f.close
    assert "".join(result) != generate_diff(filename1, filename2, "invalid_format")
