#!/usr/bin/env python
from gendiff.model.meta import add_meta


REMOVED = "removed"
ADDED = "added"
MATCHED = "unchanged"
CHANGED1 = "changed1"
CHANGED2 = "changed2"
NESTED = "nested"


def get_diff_type_diff(dct, k, diff, level):
    dif = []
    dct2 = {}
    if hasattr(dct[k], "__delitem__") and isinstance(dct[k], list) is False:
        [dct2.update({item: dct[item]}) for item in [k]]
        dif.extend(matches_one_file(dct2, diff, level)[0])
    else:
        dif.extend(add_meta(k, dct[k], diff, level))
    return dif


def get_diff_keyses(dct_src1, dct_src2, level):
    dct12 = dct22 = dct_inner = {}
    diff = []

    def get_keyses(dct1, dct2):
        dct12 = list(set(dct1.keys()) - set(dct2.keys()))
        dct21 = list(set(dct2.keys()) - set(dct1.keys()))
        dct = list(set(dct1.keys()) & set(dct2.keys()))
        return dct12, dct21, dct

    def get_dict(dct1, dct2, dct):
        dct12 = {}
        dct22 = {}
        dct_inner = {}
        [dct12.update({item: dct_src1[item]}) for item in dct1]
        [dct22.update({item: dct_src2[item]}) for item in dct2]
        [dct_inner.update({item: dct_src2[item]}) for item in dct]
        return dct12, dct22, dct_inner

    k1, k2, k3 = get_keyses(dct_src1, dct_src2)
    dct12, dct22, dct_inner = get_dict(k1, k2, k3)
    diff.extend(matches_one_file(dct12, REMOVED, level + 1))
    diff.extend(matches_one_file(dct22, ADDED, level + 1))
    diff.extend(matches_two_files(dct_inner, dct_src1, dct_src2, level + 1))
    return diff


def matches_one_file(obj, type, level):
    model = []
    if isinstance(obj, dict) is False:
        model.append(add_meta(obj, None, MATCHED, level))
        return model
    for k, v in obj.items():
        dif1 = []
        dif1.extend(add_meta(k, v, type, level))
        if hasattr(v, "__delitem__"):
            dif1.append(matches_one_file(v, MATCHED, level + 1))
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
                dif1.extend(add_meta(k, dict1[k], CHANGED1, level))
                dif2.extend(add_meta(k, dict2[k], CHANGED2, level))
            else:
                dif1.extend(add_meta(k, dict1[k], MATCHED, level))
        elif (dict1[k].__class__ != dict2[k].__class__):
            # тип значений разный. Проверяем, есть ли потомки и проходим по ним
            dif1.extend(get_diff_type_diff(dict1, k, CHANGED1, level))
            dif2.extend(get_diff_type_diff(dict2, k, CHANGED2, level))
        elif hasChild1 and hasChild2:
            # значения имеют дочерние элементы. Перебираем все значения
            dif1.extend(add_meta(k, dict1[k], NESTED, level))
            dif1.extend([get_diff_keyses(dict1[k], dict2[k], level)])
        model.append(dif1)  # головной элемент
        model.append(dif2) if len(dif2) else None
    return model


def model_building(dict1, dict2):
    model = []
    model.extend(get_diff_keyses(dict1, dict2, 0))
    # f = open("MODEL.TXT", "w")
    # f.write(str(model))
    # f.close()
    return model
