import zipfile
import os
d = {}


def read_from_zip():
    with zipfile.ZipFile("2021-archive.zip", "r") as f:
        list_of_files = f.namelist()
        print(list_of_files)
        for elem in list_of_files:
            ext = os.path.splitext(elem)[-1]
            if ext == ".txt":
                file1 = f.open(elem, 'r')
                lines = file1.readlines()
                for line in lines:
                    d[line.decode().replace("\n", "")] = elem

