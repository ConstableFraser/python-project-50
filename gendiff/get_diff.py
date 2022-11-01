#!/usr/bin/env python
from gendiff.parser.parser import parser
from gendiff.model.model_builder import model_building


def get_diff(file1, file2):
    dict1, dict2 = parser(file1, file2)
    if not dict1 or not dict2:
        return None
    return model_building(dict1, dict2)
