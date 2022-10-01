import pytest
import json
from gendiff.generate_diff import generate_diff


def test_correct1():
    f1 = "tests/fixtures/json/json1.json"
    f2 = "tests/fixtures/json/json2.json"
    result = "tests/fixtures/json/result.txt"
    f3 = open(result)
    result_list = f3.readlines()
    f3.close()
    result = ""
    for item in result_list:
        result += item
    assert result == generate_diff(f1, f2)


def test_nosuchfile():
    f1 = "tests/fixtures/json/notexist.json"
    f2 = "tests/fixtures/json/json2.json"
    assert None == generate_diff(f1, f2)


def test_correct2():
    f1 = "tests/fixtures/json/json2.json"
    f2 = "tests/fixtures/json/json1.json"
    result = "tests/fixtures/json/result2.txt"
    f3 = open(result)
    result_list = f3.readlines()
    f3.close()
    result = ""
    for item in result_list:
        result += item
    assert result == generate_diff(f1, f2)
