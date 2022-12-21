#!/usr/bin/env python


ADDED = "added"
REMOVED = "removed"
UNCHANGED = "unchanged"
CHANGED = "changed"
NESTED = "nested"


def adding_node(dict1, dict2, k, type):
    node = {}
    node[k] = {"value": dict1[k]}
    node[k].update({"type": type})
    old_value = dict2[k] if dict2 else None
    node[k].update({"old_value": old_value}) if dict2 else None
    return node


def walk_for_nodes(dict1, dict2):
    model = {}
    all_keys = sorted(set(dict1) | set(dict2))
    for k in all_keys:
        isAdded = all([k not in dict1, k in dict2])
        isRemoved = all([k in dict1, k not in dict2])

        if isAdded:
            model.update(adding_node(dict2, None, k, ADDED))
        elif isRemoved:
            model.update(adding_node(dict1, None, k, REMOVED))
        elif isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
            v = walk_for_nodes(dict1[k], dict2[k])
            model.update(adding_node({k: v}, None, k, NESTED))
        elif dict1[k] != dict2[k]:
            model.update(adding_node(dict2, dict1, k, CHANGED))
        else:
            model.update(adding_node(dict1, None, k, UNCHANGED))
    return model


def model_building(dict1, dict2):
    return walk_for_nodes(dict1, dict2)
