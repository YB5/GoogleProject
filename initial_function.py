import zipfile
import os
from itertools import permutations
d = {}
d_final = {}

def read_from_zip():
    with zipfile.ZipFile("wave.zip", "r") as f:
        list_of_files = f.namelist()
        for elem in list_of_files:
            ext = os.path.splitext(elem)[-1]
            if ext == ".txt":
                file1 = f.open(elem, 'r')
                lines = file1.readlines()
                for line in lines:
                    tmp = line.decode().replace("\n","").split()
                    n = len(tmp)
                    for i in range(n+1):
                        for j in range(i+1, n+1):
                           sli = " ".join(tmp[i:j])
                           d[sli] = [" ".join(tmp), elem,i]
    for key in d:
        if len(str(key).split()) not in d_final.keys():
            d_final[(len(str(key).split()))]=[]
        d_final[(len(str(key).split()))].append({key:d[key]})




read_from_zip()
print(d_final)