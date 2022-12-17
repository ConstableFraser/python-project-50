import pytest
from gendiff.generate_diff import generate_diff
from gendiff.parser.parse import get_content
import json


@pytest.mark.parametrize(
    "file1,file2,result,format",
    [("tests/fixtures/json/json1.json",
      "tests/fixtures/json/json2.json",
      "tests/fixtures/result.txt", "stylish"),
     ("tests/fixtures/yaml/yaml1.yml",
      "tests/fixtures/yaml/yaml2.yml",
      "tests/fixtures/result.txt", "stylish"),
     ("tests/fixtures/yaml/yaml2.yml",
      "tests/fixtures/yaml/yaml1.yml",
      "tests/fixtures/result_revert.txt", "stylish"),
     ("tests/fixtures/json/json2.json",
      "tests/fixtures/json/json1.json",
      "tests/fixtures/result_revert.txt", "stylish"),
     ("tests/fixtures/json/json1.json",
      "tests/fixtures/json/json2.json",
      "tests/fixtures/result_jsonf.txt", "json"),
     ("tests/fixtures/json/json2.json",
      "tests/fixtures/json/json1.json",
      "tests/fixtures/result_jsonf_revert.txt", "json"),
     ("tests/fixtures/json/json1.json",
      "tests/fixtures/json/json2.json",
      "tests/fixtures/result_plain.txt", "plain"),
     ("tests/fixtures/json/json2.json",
      "tests/fixtures/json/json1.json",
      "tests/fixtures/result_plain_revert.txt", "plain"),
     ("tests/fixtures/json/json_lst1.json",
      "tests/fixtures/json/json_lst2.json",
      "tests/fixtures/result_plain_list.txt", "plain")])
def test_corrects(file1, file2, result, format):
    result = get_content(result)
    assert "".join(result) == generate_diff(file1,
                                            file2,
                                            format)


@pytest.mark.parametrize(
    "file1,file2,result,format",
    [pytest.param("tests/fixtures/json/json1.json",
                  "tests/fixtures/json/json2.json",
                  "tests/fixtures/result_lst.txt",
                  "stylish",
                  marks=pytest.mark.xfail),
     pytest.param("tests/fixtures/json/json1.json",
                  "tests/fixtures/json/json2.json",
                  "tests/fixtures/result_lst.txt",
                  "UNCORRECT_FORMAT",
                  marks=pytest.mark.xfail),
     pytest.param("tests/fixtures/json/json1.json",
                  "TESTS/FAIL_FILE.JSON",
                  "tests/fixtures/result_lst.txt",
                  "plain",
                  marks=pytest.mark.xfail)])
def test_fails(file1, file2, result, format):
    result = get_content(result)
    try:
        output = generate_diff(file1, file2, format)
    except FileNotFoundError:
        assert output is None
    assert "".join(result) == output


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
    dct = ""
    model = ""
    with open("tests/fixtures/file_to_load.json") as f1:
        dct = json.loads(f1.read())
    with open("tests/fixtures/model.json") as f2:
        model = json.loads(f2.read())
    assert dct == model
