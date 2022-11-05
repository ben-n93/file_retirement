"""
This script deletes old versions (based on creation time) of files that
feature the specified string in the file name.
"""

import os
import argparse

parser = argparse.ArgumentParser(description="Delete old versions of files \
    with the specified string in the file name, located in the specified \
    directory.")

parser.add_argument(
    "--directory_path", "--d", help="Directory path of the files you wanted \
    deleted.", required=True
)
parser.add_argument(
    "--file_name", "--f", help="Name of the files you want to delete. \
    It does not have to be a complete file name, just a unique string that \
    appears in the file name.", required=True
)

args = parser.parse_args()

def delete_old_files(directory, file_name):
    """In the specified directory, delete old versions of files
    with a specified string in the file name. """

    files_dictionary = {}
    directory_contents = os.listdir(directory)

    for file in directory_contents:
        file = os.path.abspath(os.path.join(directory, file))
        if str(file_name) in file:
            files_dictionary[file] = os.path.getctime(file)

    try:
        latest_file_creation_date = max(files_dictionary.values())
    except ValueError:
        print("Files not found in directory.")

    for file, file_ctime in files_dictionary.items():
        if file_ctime != latest_file_creation_date:
            os.remove(file)


if __name__ == "__main__":
    delete_old_files(args.directory_path, args.file_name)
