import argparse
from gendiff.generate_diff import generate_diff
from gendiff.formatter.format_stylish import stylish

DESCRIPTION = "Compares two configuration files and shows a difference."
HELP = "set format of output"


def parse_args():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-f", "--format", type=str, help=HELP)
    args = vars(parser.parse_args())
    return generate_diff(args['first_file'], args['second_file'], stylish)
