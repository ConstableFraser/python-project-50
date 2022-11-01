#!/usr/bin/env python
from gendiff.model.add_meta import add_meta


FIRST_FILE = "-"
SECOND_FILE = "+"
COMMON_FILE = " "
INDENT = 4


def get_diff_type_diff(dct, k, diff, level):
    dif = []
    dct2 = {}
    if hasattr(dct[k], "__delitem__") and isinstance(dct[k], list) is False:
        [dct2.update({item: dct[item]}) for item in [k]]
        dif.extend(matches_one_file(dct2, diff, level)[0])
    else:
        dif.extend(add_meta(k, dct[k], diff, level))
    return dif


def get_diff_keyses(dct1, dct2, level):
    dct = {}
    diff = []
    keyses2 = set(dct1.keys()) - set(dct2.keys())
    if len(keyses2):
        [dct.update({item: dct1[item]}) for item in keyses2]
        diff.extend(matches_one_file(dct, FIRST_FILE, level + 1))
    dct = {}
    keyses2 = set(dct2.keys()) - set(dct1.keys())
    if len(keyses2):
        [dct.update({item: dct2[item]}) for item in keyses2]
        diff.extend(matches_one_file(dct, SECOND_FILE, level + 1))
    dct = {}
    keyses2 = set(dct1.keys()) & set(dct2.keys())
    if len(keyses2):
        [dct.update({item: dct2[item]}) for item in keyses2]
        diff.extend(matches_two_files(dct, dct1, dct2, level + 1))
    return diff


def matches_one_file(obj, differ, level):
    model = []
    if isinstance(obj, dict) is False:
        model.append(add_meta(obj, None, COMMON_FILE, level))
        return model
    for k, v in obj.items():
        dif1 = []
        dif1.extend(add_meta(k, v, differ, level))
        if hasattr(v, "__delitem__"):
            dif1.append(matches_one_file(v, COMMON_FILE, level + 1))
        model.append(dif1)
    return model


def matches_two_files(dct, dict1, dict2, level):
    model = []
    for k, _ in dct.items():
        dif1 = []
        dif2 = []
        hasChild1 = hasattr(dict1[k], "__delitem__")
        hasChild2 = hasattr(dict2[k], "__delitem__")
        isList1 = isinstance(dict1[k], list)
        isList2 = isinstance(dict2[k], list)

        if (isList1 and isList2) or (not hasChild1 and not hasChild2):
            # если элементы - это списки, ИЛИ у значений нет детей
            if dict1[k] != dict2[k]:
                dif1.extend(add_meta(k, dict1[k], FIRST_FILE, level))
                dif2.extend(add_meta(k, dict2[k], SECOND_FILE, level))
            else:
                dif1.extend(add_meta(k, dict1[k], COMMON_FILE, level))
        elif (dict1[k].__class__ != dict2[k].__class__):
            # тип значений разный. Проверяем, есть ли потомки и проходим по ним
            dif1.extend(get_diff_type_diff(dict1, k, FIRST_FILE, level))
            dif2.extend(get_diff_type_diff(dict2, k, SECOND_FILE, level))
        elif hasChild1 and hasChild2:
            # значения имеют дочерние элементы. Перебираем все значения
            dif1.extend(add_meta(k, dict1[k], COMMON_FILE, level))
            dif1.extend([get_diff_keyses(dict1[k], dict2[k], level)])
        model.append(dif1)  # головной элемент
        model.append(dif2) if len(dif2) else None
    return model


def model_building(dict1, dict2):
    model = []
    model.extend(get_diff_keyses(dict1, dict2, 0))
    return model
