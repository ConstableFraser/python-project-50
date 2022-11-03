#!/usr/bin/env python
from itertools import chain
from gendiff.formatter.utilities import normalize, get_sort_map


def chain_list(lst):
    if not isinstance(lst[0], list):
        return [lst]
    lst2 = lst
    while len(lst2) == 1:
        lst2 = list(chain(*lst2))
    return lst2


def get_index(element, branch, count):
    cnt = list(chain(*branch)).count(element)
    if count > cnt or not cnt:
        return None
    i = 0
    lst = []
    for item in branch:
        if item.count(element):
            lst.extend([i])
        i += 1

    return lst[count - 1]


def added(fullname, element, branch):
    lst = []
    lst = chain_list(branch)
    cnt = list(chain(*lst)).count(element)
    if cnt == 2:
        return ""
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
    output += " to " + normalize(value_to, "plain")
    output += "\n"
    return output


def fullmatch(fullname, element, branch):
    return ""


def removed_updated(fullname, element, branch):
    dct = {
        "1": removed,
        "2": updated
    }
    branch = chain_list(branch)
    index = str(list(chain(*branch)).count(element))
    return dct[index](fullname, element, branch)


def plain(model):
    differs = {
        "-": removed_updated,
        "+": added,
        " ": fullmatch
    }

    def browse_for_branch(branch, name):
        output = ""
        dct = {}
        dct = branch[2]
        fullname = name + "." + branch[0] if dct["level"] != 1 else branch[0]
        output += differs[dct["differ"]](fullname, branch[0], branch)
        lst = get_sort_map(branch[3])
        for element in lst:
            dct2 = {}
            dct2 = branch[3][element[1]][2]
            value = branch[3][element[1]]
            if dct2["hasChild"] and dct2["differ"] == " ":
                output += browse_for_branch(value, fullname)
                continue
            name = fullname
            fullname += "." + value[0]
            output += differs[dct2["differ"]](fullname, value[0], branch[3])
            fullname = name
        return output
    lst = []
    lst = get_sort_map(model)
    output = ""
    for element in lst:
        output += browse_for_branch(model[element[1]], element[0])
    return output
