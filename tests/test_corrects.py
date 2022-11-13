import pytest
from gendiff.generate_diff import generate_diff
from gendiff.get_content import get_content
import json


@pytest.mark.parametrize(
    "files,result,format", [([["tests/fixtures/json/json1.json"],
                             ["tests/fixtures/json/json2.json"]],
                             "tests/fixtures/result.txt", "stylish"),
                            ([["tests/fixtures/yaml/yaml1.yml"],
                             ["tests/fixtures/yaml/yaml2.yml"]],
                             "tests/fixtures/result.txt", "stylish"),
                            ([["tests/fixtures/yaml/yaml2.yml"],
                             ["tests/fixtures/yaml/yaml1.yml"]],
                             "tests/fixtures/result_revert.txt", "stylish"),
                            ([["tests/fixtures/json/json2.json"],
                             ["tests/fixtures/json/json1.json"]],
                             "tests/fixtures/result_revert.txt", "stylish"),
                            ([["tests/fixtures/json/json1.json"],
                             ["tests/fixtures/json/json2.json"]],
                             "tests/fixtures/result_jsonf.txt", "json"),
                            ([["tests/fixtures/json/json2.json"],
                             ["tests/fixtures/json/json1.json"]],
                             "tests/fixtures/result_jsonf_revert.txt", "json"),
                            ([["tests/fixtures/json/json1.json"],
                             ["tests/fixtures/json/json2.json"]],
                             "tests/fixtures/result_plain.txt", "plain"),
                            ([["tests/fixtures/json/json2.json"],
                             ["tests/fixtures/json/json1.json"]],
                             "tests/fixtures/result_plain_revert.txt", "plain"),
                            ([["tests/fixtures/json/json_lst1.json"],
                             ["tests/fixtures/json/json_lst2.json"]],
                             "tests/fixtures/result_plain_list.txt", "plain"),
                            pytest.param([["tests/fixtures/json/json1.json"],
                                         ["tests/fixtures/json/json2.json"]],
                                         "tests/fixtures/result_lst.txt",
                                         "stylish",
                                         marks=pytest.mark.xfail),
                            pytest.param([["tests/fixtures/json/json1.json"],
                                         ["tests/fixtures/json/json2.json"]],
                                         "tests/fixtures/result_lst.txt",
                                         "UNCORRECT_FORMAT",
                                         marks=pytest.mark.xfail),
                            pytest.param([["tests/fixtures/json/json1.json"],
                                         ["TESTS/FAIL_FILE.JSON"]],
                                         "tests/fixtures/result_lst.txt",
                                         "plain",
                                         marks=pytest.mark.xfail)])
def test_corrects(files, result, format):
    result = get_content(result)
    assert "".join(result) == generate_diff(files[0][0],
                                            files[1][0],
                                            format)


@pytest.fixture
def correct_json():
    file1 = "tests/fixtures/json/json1.json"
    file2 = "tests/fixtures/json/json2.json"
    return file1, file2


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
