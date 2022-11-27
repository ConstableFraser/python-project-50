#!/usr/bin/env python
from itertools import chain
from gendiff.formatter.utilities import normalize, get_sort_map, get_index


def plain(model):
    lst = []
    lst = get_sort_map(model)
    output = ""
    output = [browse_for_branch(model[e[1]], e[0]) for e in lst]
    return "".join(output).strip("\n")


def browse_for_branch(branch, name):
    dict_map = {
        "removed": removed,
        "added": added,
        "unchanged": matched,
        "modified1": updated,
        "modified2": matched,
        "nested": matched
    }
    output = ""
    meta = {}
    meta = branch[2]
    type = dict_map[meta["type"]]
    key = branch[0]
    fullname = name + "." + key if meta["level"] != 1 else key
    output += type(fullname, key, branch)
    lst = get_sort_map(branch[3])
    for element in lst:
        meta = branch[3][element[1]][2]
        type = dict_map[meta["type"]]
        value = branch[3][element[1]]
        if meta["hasChild"] and (meta["type"] in ["unchanged", "nested"]):
            output += browse_for_branch(value, fullname)
        else:
            name = fullname
            fullname += "." + value[0]
            output += type(fullname, value[0], branch[3])
            fullname = name
    return output


def chain_list(lst):
    if not isinstance(lst[0], list):
        return [lst]
    lst2 = lst
    while len(lst2) == 1:
        lst2 = list(chain(*lst2))
    return lst2


def added(fullname, element, branch):
    lst = []
    lst = chain_list(branch)
    index = get_index(element, lst, 1)
    value = lst[index][1]
    output = ""
    output += f"Property '{fullname}' "
    output += "was added with value: "
    output += normalize(value, "plain") + "\n"
    return output


def removed(fullname, element, branch):
    output = ""
    output += f"Property '{fullname}' was removed\n"
    return output


def updated(fullname, element, branch):
    lst = []
    lst = chain_list(branch)
    output = ""
    output += f"Property '{fullname}' was updated."
    value_from = lst[get_index(element, branch, 1)][1]
    output += " From " + normalize(value_from, "plain")
    value_to = lst[get_index(element, branch, 2)][1]
    output += " to " + normalize(value_to, "plain") + "\n"
    return output


def matched(fullname, element, branch):
    return ""
