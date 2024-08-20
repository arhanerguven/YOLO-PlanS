import os

main_path = "/media/arhan-erguven/Data/YOLO_TestR"

for folder_name in os.listdir(main_path):
    folder_inside = os.path.join(main_path, folder_name)
    for file_name in os.listdir(folder_inside):
        file_path = os.path.join(folder_inside, file_name)
        if file_path.endswith(".txt"):
            with open(file_path, "r") as f:
                for line in f:
                    data = line.strip().split(" ")
                    if data[0] == "9":
                        os.remove(file_path)
                        os.remove(file_path.replace(".txt", ".jpg"))
                        break