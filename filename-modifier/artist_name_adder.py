import os
import sys
import re


def main():
    arg_len = len(sys.argv)
    if arg_len > 3:
        print("Use one of the following forms :")
        print("1) python artist_name_adder.py.py")
        print("2) python artist_name_adder.py.py <directory>")
        print("3) python artist_name_adder.py.py <directory> <artist name>")
    else:
        if arg_len == 1:
            dir_path, artist_name = takeInput('console')
        else:
            dir_path, artist_name = takeInput('arguments')
        if not os.path.exists(dir_path):
            print('Requested directory does not exist')
        else:
            traverse(dir_path, artist_name, 0)
            print("Rename the above shown changes? (y/n) : ", end="")
            c = input()
            if c.lower() == 'y':
                traverse(dir_path, artist_name, 1)
                print("Renaming Done !")


def takeInput(mode):
    if mode=='arguments':
        dir_path = sys.argv[1]
        artist_name = sys.argv[2]
    elif mode=='console':
        print("Directory path : ")
        dir_path = input()
        print("Artist name (leave blank to use folder name instead) : ")
        artist_name = input()
        if artist_name == "":
            if not dir_path.endswith("/"):
                dir_path = dir_path + "/"
            artist_name = (dir_path.split("/"))[-2]
    return dir_path, artist_name


def traverse(dir_path, artist_name, rename_mode):
    if not(dir_path.endswith("/")):
        dir_path = dir_path + "/"
    for file_name in os.listdir(dir_path):
        fpath = dir_path + file_name
        if os.path.isfile(fpath):
            modify_name(dir_path, file_name, artist_name, rename_mode)
        elif os.path.isdir(fpath):
            traverse(fpath, artist_name, rename_mode)


def modify_name(dir_path, file_name, artist_name, rename_mode):
    new_file_name = artist_name + " - " + file_name
    if rename_mode == 1:
        os.rename(dir_path + file_name, dir_path + new_file_name)
    else:
        print("Old name :", file_name)
        print("New name :", new_file_name)
        print("")


if __name__ == '__main__':
    main()
