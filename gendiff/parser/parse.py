#!/usr/bin/env python
import os.path
import yaml
import json


def parse(object_data, format):
    if format is None:
        return None
    formats = {
        ".json": json.loads,
        ".yaml": yaml.safe_load,
        ".yml": yaml.safe_load
    }
    return formats[format](object_data)


def get_content(filename):
    with open(filename) as f:
        return f.read()


def get_extension(filepath):
    if not os.path.isfile(filepath):
        return None
    _, ext = os.path.splitext(filepath)
    ext = ext.lower()
    return ext if len(ext) > 0 else None
