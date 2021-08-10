import threading
import zipfile
import os

d = {}
d_final = {}


class tt(threading.Thread):
    def __init__(self, f, elem):
        super(tt, self).__init__()
        self.f = f
        self.elem = elem
        self.di = {}

    def run(self):
        lines = self.f
        for line in lines:
            tmp = line.decode().replace("\n", "").split()
            n = len(tmp)
            for i in range(n + 1):
                for j in range(i + 1, n + 1):
                    sli = " ".join(tmp[i:j])
                    self.di[sli] = [" ".join(tmp), self.elem, i]



def read_from_zip():
    with zipfile.ZipFile("2021-archive.zip", "r") as f:
        list_of_files = f.namelist()
        for elem in list_of_files:
            ext = os.path.splitext(elem)[-1]
            if ext == ".txt":
                print(elem)
                file1 = f.open(elem, 'r')
                lines = file1.readlines()
                thr = []
                for i in range(0,len(lines),len(lines)//5):
                    thred = tt(lines[i:i+len(lines)//5],elem)
                    thr.append(thred)
                for i in thr:
                    i.start()

                #_thread.start_new_thread(some,(file1,elem))
                # lines = file1.readlines()
                # for line in lines:
                #     tmp = line.decode().replace("\n", "").split()
                #     n = len(tmp)
                #     for i in range(n + 1):
                #         for j in range(i + 1, n + 1):
                #             sli = " ".join(tmp[i:j])
                #             d[sli] = [" ".join(tmp), elem, i]

    for i in thr:
        i.join()
    for i in thr:
        d.update(i.di)
    for key in d:
        if len(str(key).split()) not in d_final.keys():
            d_final[(len(str(key).split()))] = []
        d_final[(len(str(key).split()))].append({key: d[key]})
