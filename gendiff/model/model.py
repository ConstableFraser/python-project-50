#!/usr/bin/env python


ADDED = "added"
REMOVED = "removed"
UNCHANGED = "unchanged"
CHANGED = "changed"
NESTED = "nested"


def get_keyses_sets(dct1, dct2):
    keys_added = list(set(dct2.keys()) - set(dct1.keys()))
    keys_removed = list(set(dct1.keys()) - set(dct2.keys()))
    keys_equal = list(set(dct1.keys()) & set(dct2.keys()))
    return keys_added, keys_removed, keys_equal


def adding_nodes_to_model(model, dicts, keyses_set, type):
    dict1 = dicts[0]
    dict2 = dicts[1]
    for k in keyses_set:
        model[k] = {"value": dict1[k]}
        model[k].update({"type": type})
        old_value = dict2[k] if dict2 else None
        model[k].update({"old_value": old_value}) if dict2 else None


def browse_nodes_equals(model, dict1, dict2, k):
    isNested = all([isinstance(dict1[k], dict),
                    isinstance(dict2[k], dict)])
    isChanged = all([dict1[k] != dict2[k], isNested is False])
    if isNested:
        v = model_building(dict1[k], dict2[k])
        adding_nodes_to_model(model,
                              [{k: v}, None],
                              {k},
                              NESTED)
    elif isChanged:
        adding_nodes_to_model(model, [dict2, dict1], {k}, CHANGED)
    else:
        adding_nodes_to_model(model, [dict1, None], {k}, UNCHANGED)


def model_building(dict1, dict2):
    model = {}
    keyses_added, keyses_removed, keyses_equal = get_keyses_sets(dict1, dict2)
    adding_nodes_to_model(model, [dict2, None], keyses_added, ADDED)
    adding_nodes_to_model(model, [dict1, None], keyses_removed, REMOVED)
    for key in keyses_equal:
        browse_nodes_equals(model, dict1, dict2, key)
    return model
