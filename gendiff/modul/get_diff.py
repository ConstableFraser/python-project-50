import json


def get_diff(file1, file2):
    dct1 = json.load(open(file1))
    dct2 = json.load(open(file2))
    result = []
    keys_set = set(tuple(dct1.keys()) + tuple(dct2.keys()))
    keys_set = sorted(keys_set)
    for item in keys_set:
        if (item in dct1) and (item in dct2) and (dct1[item] == dct2[item]):
            result.extend([[' ', item, dct1[item]]])
            continue
        elif (item in dct1) and (item in dct2) and (dct1[item] != dct2[item]):
            result.extend([['-', item, dct1[item]], ['+', item, dct2[item]]])
            continue
        if (item in dct1):
            result.extend([['-', item, dct1[item]]])
        else:
            result.extend([['+', item, dct2[item]]])
    return result
