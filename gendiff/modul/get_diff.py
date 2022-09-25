#!/usr/bin/env python

import json
import os.path


MINUS = '-'
PLUS = '+'
OK = ' '


def get_diff(file1, file2):
    f1 = os.path.isfile(file1)
    f2 = os.path.isfile(file2)
    if not f1 or not f2:
        return None
    dct1 = json.load(open(file1))
    dct2 = json.load(open(file2))
    result = []
    keys_set = set(tuple(dct1.keys()) + tuple(dct2.keys()))
    keys_set = sorted(keys_set)
    for item in keys_set:
        if (item in dct1) and (item in dct2):
            if dct1[item] == dct2[item]:
                result.extend([[OK, item, dct1[item]]])
                continue
            else:
                result.extend([[MINUS, item, dct1[item]]])
                result.extend([[PLUS, item, dct2[item]]])
                continue
        elif (item in dct1):
            result.extend([[MINUS, item, dct1[item]]])
        else:
            result.extend([[PLUS, item, dct2[item]]])
    return result
