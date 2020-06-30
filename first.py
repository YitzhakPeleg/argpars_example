from trains import Task
from argparse import ArgumentParser


def main():
    parser = ArgumentParser()
    parser.add_argument("-a", default="A")
    args, unknown_arguments = parser.parse_known_args()  # parse only known arguments.
    print(f"{__file__}: args = {args}")
    import second
    second.main(unknown_arguments)  # call the main of command with additional args


if __name__ == '__main__':
    main()
