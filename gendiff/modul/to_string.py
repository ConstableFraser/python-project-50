def to_string(diff):
    var = "{\n"
    for item in diff:
        var += "  " + str(item[0]) + " "
        var += str(item[1]) + ": "
        var += str(item[2]) + "\n"
    var += "}\n"
    return var
