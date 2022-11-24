#!/usr/bin/env python

from gendiff.parser.parse import parse, get_extension, get_content
from gendiff.formatter.format_stylish import stylish
from gendiff.formatter.format_plain import plain
from gendiff.formatter.format_json import jsonf
from gendiff.model.model import model_building


def generate_diff(file1, file2, format_name="stylish"):
    dct = {
        "plain": plain,
        "stylish": stylish,
        "json": jsonf,
        None: stylish
    }
    if format_name not in dct.keys():
        return None
    data_file1 = get_content(file1)
    data_file2 = get_content(file2)
    dict1 = parse(data_file1, get_extension(file1))
    dict2 = parse(data_file2, get_extension(file2))
    model = model_building(dict1, dict2)
    return dct[format_name](model) if model is not None else None
