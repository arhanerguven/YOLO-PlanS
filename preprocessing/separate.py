import os
import shutil

mother_path = "/media/arhan-erguven/Data/train"



for file in os.listdir(os.path.join(mother_path, "images")):
    if file.endswith(".txt"):
        shutil.move(os.path.join(mother_path, "images", file), os.path.join(mother_path, "labels", file))