from trains import Task
from argparse import ArgumentParser

init_task_before_second_parsing = True

parser = ArgumentParser()
parser.add_argument("-a", default="A")
args, unknown_arguments = parser.parse_known_args()  # parse only known arguments.
print(f"{__file__}: parsed args = {args}")
import second
second.main(init_task_before_second_parsing, unknown_arguments)  # call the main of command with additional args


print(f"parameters from task {Task.current_task().id}")
for key, val in Task.current_task().get_parameters_as_dict().items():
    print(f"{key} = {val}")
