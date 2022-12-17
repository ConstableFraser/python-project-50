import json


def jsonf(tree):
    return json.dumps(tree, sort_keys=True)
