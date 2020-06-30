from trains import Task
from argparse import ArgumentParser


def main(init_task_before_second_parsing: bool, incoming_args: list):
    parser = ArgumentParser(prog="")
    parser.add_argument("-b", default="B")
    if init_task_before_second_parsing:
        Task.init("argparsing", "init task before second parsing", reuse_last_task_id=False)
        args, unknown_arguments = parser.parse_known_args(incoming_args)  # parse only known arguments.
    else:
        args, unknown_arguments = parser.parse_known_args(incoming_args)  # parse only known arguments.
        Task.init("argparsing", "init task after second parsing", reuse_last_task_id=False)
    print(f"{__file__}: parsed args = {args}")
