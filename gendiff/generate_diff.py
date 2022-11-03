#!/usr/bin/env python

from gendiff.get_diff import get_diff
from gendiff.formatter.format_stylish import stylish
from gendiff.formatter.format_plain import plain


def generate_diff(file1, file2, format_name="stylish"):
    dct = {
        "plain": plain,
        "stylish": stylish,
        None: stylish
    }
    if format_name not in dct.keys():
        return None
    model = get_diff(file1, file2)
    return dct[format_name](model) if model is not None else None
