import os
import re

all_files = os.listdir()
print(all_files)
only_ppk =[]
for file in all_files:
    if(re.search(r"\.ppk",file)):
        only_ppk.append(file)

print("\n",only_ppk)

for file in only_ppk:
    os.remove(file)

#print(os.listdir())