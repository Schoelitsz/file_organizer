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
        # Iterate through the files in the root directory
        for file in os.listdir(root_directory):
            full_file_path = os.path.join(root_directory, file)

            # Check if it's a file and not a directory
            if os.path.isfile(full_file_path):
                # Get the file extension
                file_name, file_extension = os.path.splitext(file)
                # Remove the dot from the extension to match folder names (e.g., 'txt' from '.txt')
                extension = file_extension[1:]

                # If the extension matches the folder name, move the file
                if extension == folder_name:
                    # Move the file to the corresponding folder
                    shutil.move(full_file_path, folder_path)
                    print(f"Moved {file} to {folder_name}")
