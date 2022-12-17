#!/usr/bin/env python
from gendiff.formatter.utilities import normalize


INDENT = 4
MARK_SIGN = 2  # '+' or '-' or ' ' at the beginning of a node


dict_map = {
    "removed": "-",
    "added": "+",
    "unchanged": " ",
    "nested": " "
}


def open_tag(type, key, level, isDict):
    output = ""
    sign = dict_map[type]
    indent = level * INDENT - MARK_SIGN
    output += " " * indent + sign + " " + key + ": "
    output += "{\n" if isDict else ""
    return output


def close_tag(level):
    output = " " * level * INDENT + "}\n"
    return output


def walk_for_dict(value, type, level):
    output = ""
    keyses = list(value.keys())
    keyses.sort()
    for k in keyses:
        isDict = isinstance(value[k], dict)
        output += open_tag("unchanged", str(k), level + 1, isDict)
        if isDict:
            output += walk_for_dict(value[k], type, level + 1)
            output += close_tag(level + 1)
            continue
        output += normalize(value[k], "stylish") + "\n"
    return output


def add_nested(tree, key, level):
    output = ""
    type = tree[key]["type"]
    node = tree[key]["value"]
    output += open_tag(type, key, level, isinstance(node, dict))
    keyses = list(node.keys())
    keyses.sort()
    for k in keyses:
        child_type = node[k]["type"]
        output += dict_func[child_type](node, k, level + 1)
    output += close_tag(level)
    return output


def add_node(node, key, level):
    output = ""
    type = node[key]["type"]
    value = node[key]["value"]
    isDict = isinstance(value, dict)
    output += open_tag(type, key, level, isDict)
    if isDict:
        output += walk_for_dict(value, "unchanged", level)
        output += close_tag(level)
        return output
    output += normalize(value, "stylish") + "\n"
    return output


def add_changed(node, key, level):
    output = ""
    value = node[key]["value"]
    old_value = node[key]["old_value"]

    for i, v in enumerate([old_value, value]):
        type = "added" if i else "removed"
        if isinstance(v, dict):
            output += open_tag(type, str(key), level, True)
            output += walk_for_dict(v, "unchanged", level)
            output += close_tag(level)
            continue
        output += open_tag(type, str(key), level, False)
        output += normalize(v, "stylish") + "\n"
    return output


dict_func = {
    "removed": add_node,
    "added": add_node,
    "unchanged": add_node,
    "nested": add_nested,
    "changed": add_changed
}


def stylish(tree):
    keyses = []
    keyses = list(tree.keys())
    keyses.sort()
    output = "{\n"
    for key in keyses:
        node_type = tree[key]["type"]
        output += dict_func[node_type](tree, key, 1)
    output += "}"
    return output
