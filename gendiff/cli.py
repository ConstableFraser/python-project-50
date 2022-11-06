import argparse
from gendiff.generate_diff import generate_diff
import typing

DESCRIPTION = "Compares two configuration files and shows a difference."
HELP = "set format of output"


def parse_args():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("frst_file", type=str)
    parser.add_argument("scnd_file", type=str)
    parser.add_argument("-f", "--format", type=str, help=HELP)
    args = vars(parser.parse_args())
    return generate_diff(args["frst_file"], args["scnd_file"], args["format"])
