import os
import glob


folder_path = "/media/arhan-erguven/Data/YOLO_Train_Data"
specific_word = "seg"

for folders in os.listdir(folder_path):
    folder_inside = os.path.join(folder_path, folders)

    search_pattern = os.path.join(folder_inside,"*")

    files_to_check = glob.glob(search_pattern)

    for file_path in files_to_check:
        if specific_word in os.path.basename(file_path):
            try:
                os.remove(file_path)
                print(f"Deleted {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

