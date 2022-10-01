#!/usr/bin/env python
from gendiff.parser.parser import parser


MINUS = '-'
PLUS = '+'
OK = ' '


def get_diff(file1, file2):
    dict1, dict2 = parser(file1, file2)
    if not dict1 or not dict2:
        return None
    result = []
    keys_set = set(tuple(dict1.keys()) + tuple(dict2.keys()))
    keys_set = sorted(keys_set)
    for item in keys_set:
        if (item in dict1) and (item in dict2):
            if dict1[item] == dict2[item]:
                result.extend([[OK, item, dict1[item]]])
                continue
            else:
                result.extend([[MINUS, item, dict1[item]]])
                result.extend([[PLUS, item, dict2[item]]])
                continue
        elif (item in dict1):
            result.extend([[MINUS, item, dict1[item]]])
        else:
            result.extend([[PLUS, item, dict2[item]]])
    return result
