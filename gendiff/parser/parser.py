#!/usr/bin/env python
import os.path
import yaml
import json


def parser(file1, file2):
    return load(file1), load(file2)


def load(file):
    if not os.path.isfile(file):
        return None
    index = file.rfind(".")
    if index < 0:
        return None
    ext = file[index + 1:].lower()
    f = open(file)
    if ext == "json":
        return json.load(f)
    elif (ext == "yaml" or ext == "yml"):
        return yaml.safe_load(f)
    else:
        return None
