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
    result = "tests/fixtures/result_jsonf.txt"
    return result


@pytest.fixture
def correct_result_revert():
    result_revert = "tests/fixtures/result_jsonf_revert.txt"
    return result_revert


def test_diff_jsonf(correct_json, correct_result):
    filename1, filename2 = correct_json
    f = open(correct_result)
    result = f.readlines()
    f.close()
    assert "".join(result) == generate_diff(filename1, filename2, "json")


def test_diff_json_revert(correct_json, correct_result_revert):
    filename1, filename2 = correct_json
    f = open(correct_result_revert)
    result = f.readlines()
    f.close()
    assert "".join(result) == generate_diff(filename2, filename1, "json")


def test_diff_json_open(correct_json):
    filename1, filename2 = correct_json
    f = open("tests/fixtures/file_to_load.json", "w")
    f.write(generate_diff(filename1, filename2, "json"))
    f.close()
    f = open("tests/fixtures/file_to_load.json")
    dct = {}
    dct = json.load(f)
    f.close()
    assert dct['group2']['value']['abc']['value'] == 12345
