#!/usr/bin/env python
from gendiff.formatter.utilities import normalize, get_sort_map

INDENT = 4
MARK_SIGN = 2  # '+' or '-' or ' ' in begine string


def browse_for_branch(branch):
    dict_map = {
        "removed": "-",
        "added": "+",
        "unchanged": " ",
        "changed1": "-",
        "changed2": "+",
        "nested": " "
    }
    output = ""
    sign = ""
    meta = {}
    meta = branch[2]
    level = meta["level"]
    type = meta["type"]
    sign = dict_map[type]
    indent = level * INDENT - MARK_SIGN
    output += " " * indent
    output += sign + " " + branch[0] + ": " + "{\n"
    lst = get_sort_map(branch[3])
    for element in lst:
        meta = branch[3][element[1]][2]
        level = meta["level"]
        type = meta["type"]
        value = branch[3][element[1]]
        sign = dict_map[type]
        indent = level * INDENT - MARK_SIGN
        if meta["hasChild"]:
            output += browse_for_branch(value)
            continue
        output += " " * indent
        output += sign + " " + value[0] + ": "
        output += normalize(value[1], "stylish") + "\n"
    output += " " * branch[2]["level"] * INDENT + "}\n"
    return output


def stylish(model):
    # собираем ключи 0 уровня
    lst = []
    lst = get_sort_map(model)
    output = "{\n"
    for element in lst:
        output += browse_for_branch(model[element[1]])
    output += "}"
    return output
