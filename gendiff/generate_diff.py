#!/usr/bin/env python

from gendiff.modul.to_string import to_string
from gendiff.modul.get_diff import get_diff


def generate_diff(file1, file2):
    diff = get_diff(file1, file2)
    return to_string(diff) if diff is not None else None
