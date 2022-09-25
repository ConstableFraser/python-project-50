import pytest
import json
from gendiff.generate_diff import generate_diff

@pytest.fixture
def files():
    return ["tests/fixtures/template/template1.json",
            "tests/fixtures/template/template2.json",
            "tests/fixtures/template/result.txt"
           ]

@pytest.fixture
def files2():
    return ["tests/fixtures/template/notexist.json",
            "tests/fixtures/template/template2.json",
           ]


def test_correct(files):
    f1 , f2, result = files
    f3 = open(result)
    result_list = f3.readlines()
    f3.close()
    str_tmp = ""
    for item in result_list:
        str_tmp += item
    assert str_tmp == generate_diff(f1, f2)

def test_nosuchfile(files2):
    f1 , f2 = files2
    assert None == generate_diff(f1, f2)
