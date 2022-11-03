import pytest
import json
from gendiff.generate_diff import generate_diff


@pytest.fixture
def correct_json():
    file1 = "tests/fixtures/json/json1.json"
    file2 = "tests/fixtures/json/json2.json"
    return file1, file2


@pytest.fixture
def correct_yaml():
    file1 = "tests/fixtures/yaml/yaml1.yml"
    file2 = "tests/fixtures/yaml/yaml2.yml"
    return file1, file2


@pytest.fixture
def correct_result():
    result = "tests/fixtures/result.txt"
    return result


@pytest.fixture
def correct_result_revert():
    result_revert = "tests/fixtures/result_revert.txt"
    return result_revert


def test_diff_json(correct_json,correct_result):
    filename1, filename2 = correct_json
    f = open(correct_result)
    result = f.readlines()
    f.close
    assert "".join(result) == generate_diff(filename1, filename2)


def test_diff_yaml(correct_yaml,correct_result):
    filename1, filename2 = correct_yaml
    f = open(correct_result)
    result = f.readlines()
    f.close
    assert "".join(result) == generate_diff(filename1, filename2)


def test_diff_json_revert(correct_json,correct_result_revert):
    filename1, filename2 = correct_json
    f = open(correct_result_revert)
    result = f.readlines()
    f.close
    assert "".join(result) == generate_diff(filename2, filename1)


def test_diff_yaml_revert(correct_yaml,correct_result_revert):
    filename1, filename2 = correct_yaml
    f = open(correct_result_revert)
    result = f.readlines()
    f.close
    assert "".join(result) == generate_diff(filename2, filename1)
