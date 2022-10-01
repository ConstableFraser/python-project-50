#!/usr/bin/env python


import pytest
from gendiff.generate_diff import generate_diff


def test_correct1():
    f1 = "tests/fixtures/yaml/yaml1.yml"
    f2 = "tests/fixtures/yaml/yaml2.yml"
    result = "tests/fixtures/yaml/result1.txt"
    f3 = open(result)
    result_list = f3.readlines()
    f3.close()
    result = ""
    for item in result_list:
        result += item
    assert result == generate_diff(f1, f2)


def test_correct2():
    f1 = "tests/fixtures/yaml/yaml2.yml"
    f2 = "tests/fixtures/yaml/yaml1.yml"
    result = "tests/fixtures/yaml/result2.txt"
    f3 = open(result)
    result_list = f3.readlines()
    f3.close()
    result = ""
    for item in result_list:
        result += item
    assert result == generate_diff(f1, f2)
