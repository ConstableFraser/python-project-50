#!/usr/bin/env python

def normalize(value, style):
    type = {
        "plain": "'",
        "stylish": ""
    }
    if isinstance(value, dict) or isinstance(value, list):
        return "[complex value]"
    dct = {
        "False": "false",
        "True": "true",
        "None": "null"
    }
    value = str(value)
    if list(dct.keys()).count(value):
        value = dct[value]
    elif value.isdigit():
        return value
    else:
        value = type[style] + value + type[style]
    return value
