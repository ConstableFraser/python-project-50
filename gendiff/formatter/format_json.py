from gendiff.formatter.utilities import get_sort_map, get_index

INDENT = 4
VALUE_INDENT = "    "


def convert(value):
    dct = {
        "False": "false",
        "True": "true",
        "None": "null"
    }
    value = str(value)
    if value in dct.keys():
        return dct[value]
    return value if value.isdigit() else '"' + str(value) + '"'


def add_value(value, meta, branch):
    output = ""
    indent = meta["level"] * INDENT
    delta = VALUE_INDENT * (meta["level"] - 1)
    output += " " * indent + delta
    delta = VALUE_INDENT * meta["level"]
    indent = meta["level"] * INDENT
    full_indent = " " * indent + delta
    output += '"' + value[0] + '": {\n' + full_indent + '"value":'
    output += " " + convert(value[1]) + ",\n"
    if meta["type"] == "modified2":
        index = get_index(value[0], branch, 1)
        output += full_indent + '"old_value":'
        output += " " + convert(branch[index][1]) + ",\n"
        output += full_indent + '"type": ' + '"updated"\n'
    else:
        output += full_indent + '"type": "' + str(meta["type"]) + '"\n'
    delta = VALUE_INDENT * (meta["level"] - 1)
    full_indent = " " * indent + delta
    output += full_indent + "}"
    return output


def browse_for_branch(branch):
    output = ""
    meta = {}
    meta = branch[2]
    indent = meta["level"] * INDENT
    delta = " " * (meta["level"] - 1) * INDENT
    full_indent = " " * indent + delta
    output += " " * indent + delta + '"' + branch[0] + '": {\n'
    output += full_indent + VALUE_INDENT + '"value": {\n'
    lst = get_sort_map(branch[3])
    for index, element in enumerate(lst):
        meta2 = branch[3][element[1]][2]
        value = branch[3][element[1]]
        if index and meta2["type"] != "modified2":
            output += ",\n"
        if meta2["type"] == "modified1":
            continue
        if meta2["hasChild"] and meta2["type"] != "modified2":
            output += browse_for_branch(value)
            output += "\n" if index + 1 == len(lst) else ""
            continue
        output += add_value(value, meta2, branch[3])
        output += "\n" if index + 1 == len(lst) else ""
    delta = " " * meta["level"] * INDENT
    full_indent = " " * indent + delta
    output += full_indent + "},\n" + full_indent
    output += '"type": ' + '"' + str(meta["type"]) + '"\n'
    delta = " " * (meta["level"] - 1) * INDENT
    full_indent = " " * indent + delta
    output += full_indent + "}"
    return output


def jsonf(model):
    # собираем ключи 0 уровня
    lst = []
    lst = get_sort_map(model)
    output = "{\n"
    for index, element in enumerate(lst):
        output += ",\n" if index else ""
        output += browse_for_branch(model[element[1]])
    output += "\n}\n"
    return output
