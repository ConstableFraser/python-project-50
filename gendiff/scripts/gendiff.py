import argparse
from gendiff.modul.to_string import to_string
from gendiff.modul.get_diff import get_diff

DESCRIPTION = "Compares two configuration files and shows a difference."
HELP = "set format of output"


def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument("-f", "--format", type=str, help=HELP)
    args = vars(parser.parse_args())
    diff = get_diff(args['first_file'], args['second_file'])
    print(to_string(diff))


if __name__ == "__main__":
    main()
