import os
import json
import math
import shutil

folder_path= "/media/arhan-erguven/Data/YOLO_Train_DataS"
dest_path = "/media/arhan-erguven/Data/val"
with open("class_det_list.json", "r") as file:
    class_data = json.load(file)



for folder_name in os.listdir(folder_path):
    classes = class_data[folder_name]
    for i in range(len(classes)):
        classes[i] = math.floor(classes[i] * 0.03)
    folder_path_inside = os.path.join(folder_path, folder_name)
    for file_name in os.listdir(folder_path_inside):
        if file_name.endswith(".txt"):
            with open(os.path.join(folder_path_inside, file_name), "r") as f:
                for line in f:
                    data = line.strip().split(" ")
                    if classes[int(data[0])]:
                        shutil.move(os.path.join(folder_path_inside, file_name.replace(".txt",".jpg")), os.path.join(dest_path, file_name.replace(".txt",".jpg")))
                        shutil.move(os.path.join(folder_path_inside, file_name), os.path.join(dest_path, file_name))
                        classes[int(data[0])] -= 1
                        break







