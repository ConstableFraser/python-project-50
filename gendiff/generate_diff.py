#!/usr/bin/env python

from gendiff.get_diff import get_diff
from gendiff.formatter.format_stylish import stylish


def generate_diff(file1, file2, formatter = stylish):
    model = get_diff(file1, file2)
    if not callable(formatter):
        return None
    return formatter(model) if model is not None else None
