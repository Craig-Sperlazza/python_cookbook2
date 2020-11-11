# This program will prompt you to enter a file path and it will return the file size

import os

def return_file_size(file_path):
    #check if the path exists
    if not os.path.exists(file_path):
        print("No Such Path Exists")
        return False

    #make sure it leads to a file
    if not os.path.isfile(file_path):
        print("This is not a file")
        return False

    print(f"This file is {os.path.getsize(file_path)} bytes")
    return True




if __name__ == '__main__':
    s = input("Please enter a file to find its size")
    return_file_size(s)