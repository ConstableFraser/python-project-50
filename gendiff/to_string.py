#!/usr/bin/env python


def to_string(diff):
    convert = ["True", "False", "None"]
    var = "{\n"
    for item in diff:
        var += "  " + str(item[0]) + " "
        var += str(item[1]) + ": "
        if str(item[2]) in convert:
            var += str(item[2]).lower() + "\n"
        else:
            var += str(item[2]) + "\n"
    var += "}\n"
    return var
