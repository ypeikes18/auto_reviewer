import sys
import argparse
from src.interactive_shell import start_interactive_shell
from src.file_explorer import map_path_to_file_contents
from src.ai_api import get_response_to_prompt


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Review code in a given directory.")
    parser.add_argument("-p", "--path", help="The path of the directory or file to review.")
    parser.add_argument("-b","--base-prompt", help="The path of the directory or file to review.")
    parser.add_argument("-s","--shell",action="store_true", help="The path of the directory or file to review.")

    args = parser.parse_args()


    if args.path is not None:
        path = args.path
        base_prompt_arg = args.base_prompt

        file_tree = map_path_to_file_contents(path) if args.path else ""
        base_prompt = base_prompt_arg + "\n\n" or f"Please review the following code in the file tree represented in the dictionary:"
        prompt = f"Please review the following code in the file tree represented in the dictionary:\n\n{file_tree}"
        response = get_response_to_prompt(prompt)
        print(response)
        sys.exit(1)

    if args.shell:
        start_interactive_shell()
        sys.exit(1)


 