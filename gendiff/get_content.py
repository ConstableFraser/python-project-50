#!/usr/bin/env python

def get_content(filename):
    with open(filename) as f:
        return f.read()
