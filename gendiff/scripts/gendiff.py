from gendiff.cli import parse_args
from gendiff.generate_diff import generate_diff


def main():
    args = parse_args()
    diff = generate_diff(args["frst_file"], args["scnd_file"], args["format"])
    print(diff)
