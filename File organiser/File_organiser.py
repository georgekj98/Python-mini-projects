import os
import subprocess
import re
import shutil


def list_file_types(all_files):
    types_list = []
    for file in all_files:
        if os.path.isfile(file):
            type = re.search(r"(\.)(\w+)$", file)
            if type[2] not in types_list:
                types_list.append(type[2])
    return types_list


def make_directories(types_list):
    for type in types_list:
        if not os.path.exists(type):
            os.mkdir(type)


def move_files(all_files):
    for file in all_files:
        if os.path.isfile(file):
            type = re.search(r"(\.)(\w+)$", file)
            try:
                shutil.move(file, type[2])
            except Exception as e:
                print(e)


all_files = os.listdir()
types = list_file_types(all_files)
make_directories(types)
move_files(all_files)
