import os
import shutil

mother_path = "/media/arhan-erguven/Data/dataset"

for folders in os.listdir(mother_path):
    splits = os.path.join(mother_path, folders)
    splits2 = "labels"
    file_folder = os.path.join(splits, splits2)
    if os.path.isdir(file_folder):
        for file in os.listdir(file_folder):
            if file.endswith(".txt"):
                with open(os.path.join(file_folder, file), "r+") as f:
                    check = False
                    for line in f:
                        data = line.strip().split(" ")
                        if data[0] == "-1":
                            data[0] = "9"
                            check = True
                        if float(data[1]) > 1:
                            data[1] = "1"
                            check = True
                        if float(data[2]) > 1:
                            data[1] = "1"
                            check = True
                        if float(data[3]) > 1:
                            data[1] = "1"
                            check = True
                        if float(data[4]) > 1:
                            data[1] = "1"
                            check = True
                        if check:
                            newline = f"{data[0]} {data[1]} {data[2]} {data[3]} {data[4]} \n"
                            f.write(newline)


