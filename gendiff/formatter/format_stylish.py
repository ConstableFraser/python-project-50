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
    output = []
    sign = dict_map[type]
    indent = level * INDENT - MARK_SIGN
    output = [" " * indent, sign, " ", key, ": "]
    output.extend("{\n") if isDict else ""
    return output


def close_tag(level):
    output = " " * level * INDENT + "}\n"
    return output


def walk_for_dict(value, level, flag):
    output = []
    keyses = list(value.keys())
    keyses.sort()
    for k in keyses:
        type = flag if flag else value[k]["type"]
        v = value[k] if flag else value[k]["value"]
        if type in ["added", "removed", "unchanged"]:
            if isinstance(v, dict):
                output.extend(open_tag(type, k, level + 1, True))
                output.extend(walk_for_dict(v, level + 1, "unchanged"))
                output.extend(close_tag(level + 1))
                continue
            output.extend(open_tag(type, k, level + 1, False))
            output.extend(normalize(v, "stylish") + "\n")
        elif type == "nested":
            output.extend(open_tag("unchanged", str(k), level + 1, True))
            output.extend(walk_for_dict(v, level + 1, None))
            output.extend(close_tag(level + 1))
        elif type == "changed":
            output.extend(add_changed(value, k, level))
    return output


def add_changed(value, k, level):
    old_value = value[k]["old_value"]
    v = value[k]["value"]
    output = []
    for i, e in enumerate([old_value, v]):
        type = "added" if i else "removed"
        if isinstance(e, dict):
            output.extend(open_tag(type, str(k), level + 1, True))
            output.extend(walk_for_dict(e, level + 1, "unchanged"))
            output.extend(close_tag(level + 1))
            continue
        output.extend(open_tag(type, str(k), level + 1, False))
        output.extend(normalize(e, "stylish") + "\n")
    return output


def stylish(tree):
    output = []
    output.append("{\n")
    output.extend(walk_for_dict(tree, 0, None))
    output.extend("}")
    return "".join(output)
