import os
import shutil
# run
# first retrieve all the names of the folders within the directory
# start with first folder, foreach file in folder
# match extension to folder name


def sortfoldersbyname(directory) -> dict:
    folders = {}
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):
            folders[item] = full_path
    return folders


def sortfilestoextention(folderdictionary, root_directory):
    for folder_name, folder_path in folderdictionary.items():
        for file in os.listdir(root_directory):
            full_file_path = os.path.join(root_directory, file)

            if os.path.isfile(full_file_path):
                file_name, file_extension = os.path.splitext(file)
                extension = file_extension[1:]

                if extension == folder_name:

                    shutil.move(full_file_path, folder_path)
                    print(f"Moved {file} to {folder_name}")
