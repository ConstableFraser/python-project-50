#!/usr/bin/env python
from gendiff.formatter.utilities import normalize


def add_removed(tree, key, path_name):
    output = ""
    fullpath = ""
    fullpath = (path_name + ".") if len(path_name) else ""
    output += f"\nProperty '{fullpath}{key}' was removed"
    return output


def add_added(tree, key, path_name):
    output = ""
    fullpath = (path_name + ".") if len(path_name) else ""
    value = normalize(tree[key]["value"], "plain")
    output += f"\nProperty '{fullpath}{key}' was added "\
              f"with value: {value}"
    return output


def add_nested(tree, key, path_name):
    output = ""
    fullpath = (path_name + ".") if len(path_name) else ""
    keyses = list(tree[key]["value"].keys())
    keyses.sort()
    value = tree[key]["value"]
    for k in keyses:
        node_type = value[k]["type"]
        output += dict_func[node_type](value, k, fullpath + str(key))
    return output


def add_changed(tree, key, path_name):
    output = ""
    value = normalize(tree[key]["value"], "plain")
    old_value = normalize(tree[key]["old_value"], "plain")
    fullpath = (path_name + ".") if len(path_name) else ""
    output += f"\nProperty '{fullpath}{key}' was updated. "\
              f"From {old_value} to {value}"
    return output


def add_unchanged(tree, key, path_name):
    return ""


dict_func = {
    "removed": add_removed,
    "added": add_added,
    "unchanged": add_unchanged,
    "nested": add_nested,
    "changed": add_changed
}


def plain(tree):
    keyses = []
    keyses = list(tree.keys())
    keyses.sort()
    output = ""
    for key in keyses:
        node_type = tree[key]["type"]
        output += dict_func[node_type](tree, key, "")
    return output[1::]
