from trains import Task
from argparse import ArgumentParser


def main(args: list):
    parser = ArgumentParser(prog="")
    parser.add_argument("-b", default="B")
    args, unknown_arguments = parser.parse_known_args()  # parse only known arguments.
    print(f"{__file__}: args = {args}")
    Task.init("argparsing", "example using defaults")
