from gendiff.cli import parse_args
from gendiff.generate_diff import generate_diff


def main():
    args = parse_args()
    return generate_diff(args["frst_file"], args["scnd_file"], args["format"])


if __name__ == "__main__":
    main()
