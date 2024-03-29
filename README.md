## Hexlet tests, linter status, code climate and test coverage:
[![Actions Status](https://github.com/ConstableFraser/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/ConstableFraser/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/7212408bfd1a84de5cde/maintainability)](https://codeclimate.com/github/ConstableFraser/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/7212408bfd1a84de5cde/test_coverage)](https://codeclimate.com/github/ConstableFraser/python-project-50/test_coverage)
[![Linter](https://github.com/ConstableFraser/python-project-50/actions/workflows/Linter.yml/badge.svg)](https://github.com/ConstableFraser/python-project-50/actions/workflows/Linter.yml)
[![Tests](https://github.com/ConstableFraser/python-project-50/actions/workflows/pytest.yml/badge.svg)](https://github.com/ConstableFraser/python-project-50/actions/workflows/pytest.yml)

## DESCRIPTION
project name: "Difference calculator"

the main purpose: find difference between 2 files (json/yaml format) and display in one of the formats

3 project objectives:
1. parse 2 files
2. compare and calculate diff
3. display diff in 3 formats: "stylish", "plain" and "json"

**additional info**

Structural scheme
![structural scheme](docs/images/scheme.jpg)

## HOW TO INSTALL AND USE
To install the program, enter the command:

```
pip install gendiff
```

For help: `gendiff -h`

usage: `gendiff [-h] [-f FORMAT] frst_file scnd_file`

## ASCIINEMA RECORDS
### step#3 (calculate diff in flat files):
[![asciicast](https://asciinema.org/a/521850.svg)](https://asciinema.org/a/521850)
### step#5 (added files YAML format):
[![asciicast](https://asciinema.org/a/525046.svg)](https://asciinema.org/a/525046)
### step#6 (calculate diff in layered files structure and added stylish display format):
[![asciicast](https://asciinema.org/a/533946.svg)](https://asciinema.org/a/533946)
### step#7 (added plain display format):
[![asciicast](https://asciinema.org/a/534728.svg)](https://asciinema.org/a/534728)
### step#8 (added json display format):
[![asciicast](https://asciinema.org/a/535297.svg)](https://asciinema.org/a/535297)
