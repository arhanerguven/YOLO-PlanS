import os
import glob

folder_path = "/media/arhan-erguven/Data/YOLO_Data_Final/"
file_pattern = "*.png"

for folder in os.listdir(folder_path):
    folder1_path = os.path.join(folder_path, folder)

    files_to_delete = glob.glob(os.path.join(folder1_path, file_pattern))

    for file_path in files_to_delete:
        try:
            os.remove(file_path)
            print(f"File deleted: {file_path}")
        except Exception as e:
            print(f"Error while deleting file: {file_path}: {e}")