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


def adding_nodes_to_model(model, dct_src, keyses_set, type, *args):
    for key in keyses_set:
        model[key] = {"value": dct_src[key]}
        model[key].update({"type": type})
        model[key].update({"old_value": args[0]}) if args else None


def browse_nodes_equals(model, dict1, dict2, key):
    isNested = all([isinstance(dict1[key], dict),
                    isinstance(dict2[key], dict)])
    isChanged = all([dict1[key] != dict2[key], isNested is False])
    if isNested:
        adding_nodes_to_model(model,
                              {key: model_building(dict1[key], dict2[key])},
                              {key},
                              NESTED)
    elif isChanged:
        adding_nodes_to_model(model, dict2, {key}, CHANGED, dict1[key])
    else:
        adding_nodes_to_model(model, dict1, {key}, UNCHANGED)


def model_building(dict1, dict2):
    model = {}
    keyses_added, keyses_removed, keyses_equal = get_keyses_sets(dict1, dict2)
    adding_nodes_to_model(model, dict2, keyses_added, ADDED)
    adding_nodes_to_model(model, dict1, keyses_removed, REMOVED)
    for key in keyses_equal:
        browse_nodes_equals(model, dict1, dict2, key)
    return model
