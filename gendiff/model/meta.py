#!/usr/bin/env python

def add_meta(k, v, differ, level):
    meta = {"isDict": isinstance(v, dict),
            "isList": isinstance(v, list),
            "hasChild": (hasattr(v, "__delitem__") and isinstance(v, dict)),
            "type": differ,
            "level": int(level)
            }
    return [k, v, meta]
