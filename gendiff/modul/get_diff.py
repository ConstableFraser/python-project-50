import json


def get_diff(file1, file2):
    dct1 = json.load(open(file1))
    dct2 = json.load(open(file2))
    result = []
    keys_set = set(tuple(dct1.keys()) + tuple(dct2.keys()))
    keys_set = sorted(keys_set)

    def matching(item):
        if (item in dct1) and (item in dct2) and (dct1[item] == dct2[item]):
            return [[' ', item, dct1[item]]]
        elif (item in dct1) and (item in dct2) and (dct1[item] != dct2[item]):
            return [['-', item, dct1[item]], ['+', item, dct2[item]]]
        if (item in dct1):
            return [['-', item, dct1[item]]]
        else:
            return [['+', item, dct2[item]]]
    result = []
    keys_set = set(tuple(dct1.keys()) + tuple(dct2.keys()))
    keys_set = sorted(keys_set)
    for item in keys_set:
        result.extend(matching(item))
    return result
