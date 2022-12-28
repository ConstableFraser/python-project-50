#!/usr/bin/env python


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


def walk_for_tree(value, level):
    output = []
    keys = list(value.keys())
    for k in keys:
        type = value[k]["type"]
        v = value[k]["value"]
        if type in ["added", "removed", "unchanged"]:
            output.extend(add_type(type, k, v, level))
        elif type == "nested":
            output.extend(open_tag("unchanged", str(k), level + 1, True))
            output.extend(walk_for_tree(v, level + 1))
            output.extend(close_tag(level + 1))
        elif type == "changed":
            output.extend(add_changed(value, k, level))
    return output


def add_type(type, k, v, level):
    output = []
    if isinstance(v, dict):
        output.extend(open_tag(type, k, level + 1, True))
        output.extend(browse_for_dict(v, level))
        output.extend(close_tag(level + 1))
        return output
    output.extend(open_tag(type, k, level + 1, False))
    output.extend(normalize(v, "stylish") + "\n")
    return output


def browse_for_dict(value, level):
    output = []
    keys = list(value.keys())
    for k in keys:
        output.extend(add_type("unchanged", k, value[k], level + 1))
    return output


def add_changed(value, k, level):
    old_value = value[k]["old_value"]
    v = value[k]["value"]
    output = []
    for i, e in enumerate([old_value, v]):
        type = "added" if i else "removed"
        if isinstance(e, dict):
            output.extend(add_type(type, k, e, level))
            continue
        output.extend(open_tag(type, str(k), level + 1, False))
        output.extend(normalize(e, "stylish") + "\n")
    return output


def normalize(value, style):
    dct = {
        "False": "false",
        "True": "true",
        "None": "null"
    }
    value = str(value)
    value = dct[value] if value in list(dct.keys()) else value
    return value


def stylish(tree):
    output = []
    output.append("{\n")
    output.extend(walk_for_tree(tree, 0))
    output.extend("}")
    return "".join(output)
