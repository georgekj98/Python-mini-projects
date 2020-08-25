import os
import subprocess
import re
from pathlib import Path

def list_file_types():
    all_files = os.listdir()
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

types = list_file_types()
make_directories(types)
