#!/usr/bin/env python
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
