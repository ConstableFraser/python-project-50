import json


def get_diff(file1, file2):
    dict1 = json.load(open(file1))
    dict2 = json.load(open(file2))
    result = []
    keys_set = set(tuple(dict1.keys()) + tuple(dict2.keys()))
    keys_set = sorted(keys_set)
    for item in keys_set:
        if (item in dict1) and (item in dict2):
            if dict1[item] == dict2[item]:
                result.extend([[' ', item, dict1[item]]])
            else:
                result.extend([['-', item, dict1[item]]])
                result.extend([['+', item, dict2[item]]])
        elif (item in dict1) is False:
            result.extend([['+', item, dict2[item]]])
        elif (item in dict2) is False:
            result.extend([['-', item, dict1[item]]])
    return result
