from file_explorer import map_path_to_file_contents
from ai_api import get_response_to_prompt
import argparse
import sys

EXIT_COMMANDS = {"e", "exit"}


def start_interactive_shell():
    print("AI Code Reviewer Shell. Type 'exit' or 'e' to quit.")
    create_variables_from_dict(commands_to_functions)
    while True:
        shell_prompt_loop_step(globals())


def close_shell():
    sys.exit(0)


def shell_prompt_loop_step(global_vars):
    user_input = input(">> ").lower()
    if user_input in EXIT_COMMANDS:
        close_shell()
    try:
        print(exec(user_input, global_vars))
    except Exception as e:
        print("Error:", e)
    return True


command_to_normalized_command = {
    "e": "exit",
    "exit": "exit",
    "r": "review",
    "review": "review"
}

commands_to_functions = {
    "review": get_response_to_prompt,
    "get_file_tree": map_path_to_file_contents,
}

def create_variables_from_dict(var_dict):
    """
    Create global variables from a dictionary where each key-value pair 
    represents a variable name and its value.

    Args:
    var_dict (dict): Dictionary of variable names and their values.
    """
    for var_name, value in var_dict.items():
        globals()[var_name] = value    


