import os


# This function deletes a file
def delete_file(dir_path):
    os.remove(dir_path)
    print("Deleted " + dir_path)


# This function deletes an empty folder
def delete_folder(dir_path):
    os.rmdir(dir_path)  # Delete folder
    print("Deleted " + dir_path)


# This function recursively checks and deletes files/folders in the directory
def check(dir_path):
    file_list = os.listdir(dir_path)  # Create list of files/folders in directory
    for x in range(len(file_list)):
        temp = dir_path + "/" + file_list[x]  # Current file/folder selected
        if os.path.isfile(temp):  # Check if item is a file
            delete_file(temp)  # Delete file
        if os.path.isdir(temp):  # Check if item is a folder
            directory = os.listdir(temp)
            if len(directory) == 0:  # Check if folder is empty
                delete_folder(temp)  # Delete Folder
            else:
                check(temp)
                delete_folder(temp)  # Delete Folder
    delete_folder(dir_path)  # Delete Folder


def main():
    start_path = input("Enter Dir: ")  # The directory the user wants to delete
    check(start_path)  # Delete everything in directory


if __name__ == "__main__":
    main()
