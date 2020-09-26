import os
from pathlib import Path

all_files = os.listdir()
for file in all_files:
    path = Path(file)
    if path.suffix == ".mcl44":
        new_name =path.stem +".mp4"
        os.rename(file,new_name)
    if path.suffix == ".mp4":
        new_name = path.stem +".mcl44"
        os.rename(file,new_name)
        
