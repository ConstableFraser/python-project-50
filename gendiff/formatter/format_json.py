from gendiff.formatter.utilities import get_sort_map, get_index

INDENT = 4
DELTA = "    "


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
    delta = DELTA * (meta["level"] - 1)
    output += " " * indent + delta
    delta = DELTA * meta["level"]
    indent = meta["level"] * INDENT
    output += '"' + value[0] + '": {\n'
    output += " " * indent + delta + '"value":'
    output += " " + convert(value[1]) + ",\n"
    if meta["differ"] == "modified2":
        index = get_index(value[0], branch, 1)
        output += " " * indent + delta + '"old_value":'
        output += " " + convert(branch[index][1]) + ",\n"
        output += " " * indent + delta
        output += '"differ": ' + '"updated"\n'
    else:
        output += " " * indent + delta
        output += '"differ": ' + '"' + str(meta["differ"]) + '"\n'
    delta = DELTA * (meta["level"] - 1)
    output += " " * indent + delta + "}"
    return output


def browse_for_branch(branch):
    output = ""
    meta = {}
    meta = branch[2]
    indent = meta["level"] * INDENT
    delta = " " * (meta["level"] - 1) * INDENT
    output += " " * indent
    output += delta + '"' + branch[0] + '": {\n'
    output += " " * indent + delta + DELTA + '"value": {\n'
    lst = get_sort_map(branch[3])
    for index, element in enumerate(lst):
        meta2 = branch[3][element[1]][2]
        value = branch[3][element[1]]
        if index and meta2["differ"] != "modified2":
            output += ",\n"
        if meta2["differ"] == "modified1":
            continue
        if meta2["hasChild"] and meta2["differ"] != "modified2":
            output += browse_for_branch(value)
            output += "\n" if index + 1 == len(lst) else ""
            continue
        output += add_value(value, meta2, branch[3])
        output += "\n" if index + 1 == len(lst) else ""
    delta = " " * meta["level"] * INDENT
    output += " " * indent + delta + "},\n"
    output += " " * indent + delta
    output += '"differ": ' + '"' + str(meta["differ"]) + '"\n'
    delta = " " * (meta["level"] - 1) * INDENT
    output += " " * indent + delta + "}"
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
