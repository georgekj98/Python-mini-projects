import os
import subprocess
import re
from pathlib import Path

def list_file_types():
    all_files = os.listdir()
    types_list = []
    for file in all_files:
        type = re.search(r"(\.)(\w+)$", file)
        if type[2] not in types_list:
            types_list.append(type[2])
    return types_list
