import pandas as pd
import os
import sys
import csv
import math


mother_path = "/media/arhan-erguven/Data/TestReal/annotations"
results_path = "/media/arhan-erguven/Data/YOLO_Data_Converted"
final_path = "/media/arhan-erguven/Data/YOLO_Data_Final"
csv_files = [f for f in os.listdir(mother_path) if f.endswith('.csv')]
width = 640
height = 480

for file_name in csv_files:
    file_path = os.path.join(mother_path, file_name)
    with open(file_path, "r") as annot_old, open(os.path.join(results_path, f"{file_name.replace('.csv','.txt')}"), "w") as annot_new:
        csv_reader = csv.reader(annot_old)
        txt_writer = csv.writer(annot_new, delimiter=" ")
        for row in csv_reader:
            new_row = list()

            new_row.append(row[0])

            if row[7] == "-1":
                new_row.append("9")
            else:
                new_row.append(row[7])

            if ((int(row[2]) + int(row[4])/2) / width) < 1:
                new_row.append(str((int(row[2]) + int(row[4])/2) / width))
            else:
                new_row.append("1.0")

            if ((float(row[3]) + float(row[5])/2) / height) < 1.0:
                new_row.append(str((float(row[3]) + float(row[5])/2) / height))
            else:
                new_row.append("1.0")

            new_row.append(str(float(row[4]) / width))
            new_row.append(str(float(row[5]) / height))

            txt_writer.writerow(new_row)

text_files = [f for f in os.listdir(results_path) if f.endswith('.txt')]

for file_name in text_files:
    folder_path = os.path.join(final_path, file_name.replace(".txt", ""))
    os.mkdir(folder_path)
    with open(os.path.join(results_path,file_name), "r") as txt_file:
        current_frame = -1
        for line in txt_file:
            row = line.strip().split(" ")
            if int(row[0]) != current_frame:
                current_frame = int(row[0])
                file_frame = str(current_frame).rjust(10,'0')
                with open(os.path.join(folder_path, f"{file_name[:-4]}_{file_frame}.txt"), "a") as final_text:
                    final_text.write(f"{row[1]} {row[2]} {row[3]} {row[4]} {row[5]} \n")
            else:
                with open(os.path.join(folder_path, f"{file_name[:-4]}_{file_frame}.txt"), "a") as final_text:
                    final_text.write(f"{row[1]} {row[2]} {row[3]} {row[4]} {row[5]} \n")




