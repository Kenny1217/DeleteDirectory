import os


# This function recursively checks and deletes files/folders in the directory
def check(dir_path):
    file_list = os.listdir(dir_path)  # Create list of files/folders in directory
    for x in range(len(file_list)):
        temp = dir_path + "/" + file_list[x]  # Current file/folder selected
        if os.path.isfile(temp):  # Check if item is a file
            print("Delete File")  # Delete file
        if os.path.isdir(temp):  # Check if item is a folder
            directory = os.listdir(temp)
            if len(directory) == 0:  # Check if folder is empty
                print("Delete Folder")  # Delete Folder
            else:
                check(temp)
                print("Delete Folder")  # Delete Folder


def main():
    start_path = input("Enter Dir: ")  # The directory the user wants to delete
    print(start_path)


if __name__ == "__main__":
    main()
