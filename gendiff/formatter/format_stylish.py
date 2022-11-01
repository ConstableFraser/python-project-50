#!/usr/bin/env python
from gendiff.formatter.normalizer import normalize

INDENT = 4
MARK_SIGN = 2  # '+' or '-' or ' ' in begine string


def get_sort_map(branch):
    lst = []
    for index, element in enumerate(branch):
        lst.append([element[0], index])
    lst.sort()
    return lst


def stylish(model):

    def browse_for_branch(branch):
        output = ""
        dct = {}
        dct = branch[2]
        output += " " * (dct["level"] * INDENT - MARK_SIGN)
        output += dct["differ"] + " " + branch[0] + ": "
        output += "{\n"
        lst = get_sort_map(branch[3])
        for element in lst:
            dct2 = {}
            dct2 = branch[3][element[1]][2]
            value = branch[3][element[1]]
            if dct2["hasChild"]:
                output += browse_for_branch(value)
                continue
            output += " " * (dct2["level"] * INDENT - MARK_SIGN)
            output += dct2["differ"] + " " + value[0] + ": "
            output += normalize(value[1]) + "\n"
        output += " " * branch[2]["level"] * INDENT
        output += "}\n"
        return output
    # собираем ключи 0 уровня
    lst = []
    lst = get_sort_map(model)
    output = "{\n"
    for element in lst:
        output += browse_for_branch(model[element[1]])
    output += "}\n"
    #print(output)
    return output
