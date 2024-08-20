import os
import shutil

# Define the paths to the two directories
dir1 = "/media/arhan-erguven/Data/TestReal/images"
dir2 = "/media/arhan-erguven/Data/YOLO_TestR"

# Iterate through the folders in the first directory
for folder_name in os.listdir(dir1):
    folder1_path = os.path.join(dir1, folder_name)

    # Check if the folder is actually a directory
    if os.path.isdir(folder1_path):

        # Check if a folder with the same name exists in the second directory
        folder2_path = os.path.join(dir2, folder_name)
        if os.path.isdir(folder2_path):

            # If it exists, merge the contents of the two folders
            for item_name in os.listdir(folder1_path):
                item1_path = os.path.join(folder1_path, item_name)
                item2_path = os.path.join(folder2_path, item_name)

                # If the item is a file or directory, move/copy it
                if os.path.isfile(item1_path) or os.path.isdir(item1_path):
                    if not os.path.exists(item2_path):
                        shutil.move(item1_path, folder2_path)  # Move the item to the second folder
                    else:
                        print(f"Conflict: {item2_path} already exists.")

        else:
            # If the folder doesn't exist in the second directory, move it there
            shutil.move(folder1_path, dir2)

print("Merge completed.")
