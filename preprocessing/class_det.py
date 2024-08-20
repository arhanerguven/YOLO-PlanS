import pandas as pd
import os
import sys
import csv
import json


def write_data(classes: list, class_data: dict, file_class_data: dict, file_name: str):
    for i in classes:
        class_data["unknown"] = classes[-1]
        class_data["human"] = classes[0]
        class_data["elephant"] = classes[1]
        class_data["lion"] = classes[2]
        class_data["giraffe"] = classes[3]
        class_data["dog"] = classes[4]
        class_data["crocodile"] = classes[5]
        class_data["hippo"] = classes[6]
        class_data["zebra"] = classes[7]
        class_data["rhino"] = classes[8]
    file_class_data[file_name] = class_data

mother_path = "/media/arhan-erguven/Data/TrainReal/annotations"
results_path = "/media/arhan-erguven/Data/YOLO_Data_Converted"
final_path = "/media/arhan-erguven/Data/YOLO_Data_Final"
csv_files = [f for f in os.listdir(mother_path) if f.endswith('.csv')]
width = 640
height = 480
file_class_data = {}
file_class_data_list = {}


for file_name in csv_files:
    file_path = os.path.join(mother_path, file_name)
    with open(file_path, "r") as annot_old:
        class_data = {}
        class_counter = [0,0,0,0,0,0,0,0,0,0]
        csv_reader = csv.reader(annot_old)
        for row in csv_reader:
            class_counter[int(row[7])] += 1
        #To write the number of instances for each class in a folder and save it as json, use this
        write_data(class_counter, class_data, file_class_data, file_name.replace(".csv",""))
        file_class_data_list[file_name.replace(".csv","")] = class_counter




with open("class_det_trainr.json", "w") as outfile:
    json.dump(file_class_data, outfile)

with open("class_det_list.json", "w") as outfile:
    json.dump(file_class_data_list, outfile)


