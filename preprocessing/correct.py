import os
import shutil

folder_path = "/media/arhan-erguven/Data/annot_folder"

for file_name in os.listdir(folder_path):
    if file_name.endswith(".png"):
        file_name_check = file_name[:21]
        for folder_name in os.listdir(folder_path):
            if not folder_name.endswith(".png") and folder_name == file_name_check:
                shutil.move(os.path.join(folder_path, file_name), os.path.join(folder_path, folder_name + file_name))

