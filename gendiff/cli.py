import argparse

DESCRIPTION = "Compares two configuration files and shows a difference."
HELP = "set format of output"


def parse_args():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("frst_file", type=str)
    parser.add_argument("scnd_file", type=str)
    parser.add_argument("-f", "--format",
                        choices=["plain", "stylish", "json"],
                        default="stylish", help=HELP)
    args = vars(parser.parse_args())
    return args
