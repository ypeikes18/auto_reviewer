import os
from typing import List
import functools


def map_path_to_file_contents(path: str):
    """
    Creates a dictionary mapping each file path to its contents within the given directory, 
    including all subdirectories.
    
    Args:
    path (str): The root directory to start the file mapping from.

    Returns:
    dict: A dictionary where keys are file paths relative to the given directory and 
          values are the contents of those files.
    """
    if os.path.isfile(path):
        return read_file_contents(path)

    if os.path.isdir(path):
        path_to_contents = {}
        for item in os.listdir(path):
            if should_ignore(path, item):
                continue
            full_item_path = os.path.join(path, item)
            if os.path.isdir(full_item_path) or os.path.isfile(full_item_path):
                path_to_contents[full_item_path] = map_path_to_file_contents(full_item_path)
        return path_to_contents

    return {}


def should_ignore(path, item):
    if is_blacklisted(item):
        return True
    full_item_path = os.path.join(path, item)
    if not is_whitelisted(item) and os.path.isfile(full_item_path):
        return True
    return False
    


def read_file_contents(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        # Handle binary file
        with open(file_path, 'rb') as file:
            return str(file.read())


def get_blacklisted() -> set:
    return file_to_set(".reviewer_blacklist")


def get_whitelisted() -> set:
    return file_to_set(".reviewer_whitelist")
    

def is_blacklisted(name: str) -> bool:
    return name in get_blacklisted()


def is_whitelisted(name: str):
    split = name.split(".")
    if len(split) > 0:
        return split[-1] in get_whitelisted()


@functools.lru_cache(maxsize=None)
def file_to_set(file_path):
    """
    Reads a file and converts each line into an element of a set.

    Args:
    file_path (str): Path to the file containing lines of file or directory names.

    Returns:
    set: A set containing the unique lines from the file.
    """
    result_set = set()

    with open(file_path, 'r') as file:
        for line in file:
            # Strip newline and other trailing whitespace characters
            cleaned_line = line.strip()
            result_set.add(cleaned_line)

    return result_set