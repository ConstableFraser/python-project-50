#!/usr/bin/env python

def normalize(value):
    value = str(value)
    value = value.replace("False", "false")
    value = value.replace("True", "true")
    value = value.replace("None", "null")
    return value
