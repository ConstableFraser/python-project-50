#!/usr/bin/env python
import os.path
import yaml
import json


def parser(file1, file2):
    return load(file1), load(file2)


def load(file):
    if not os.path.isfile(file):
        return None
    _, ext = os.path.splitext(file)
    ext = ext.lower()
    f = open(file)
    if ext == ".json":
        return json.load(f)
    elif (ext == ".yaml" or ext == ".yml"):
        return yaml.safe_load(f)
    else:
        return None
