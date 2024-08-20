import os
import shutil


def flatten_directory(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, _, files in os.walk(src_dir):
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, file)
            shutil.copyfile(src_file, dest_file)

src_train_images = "/media/arhan-erguven/Data/train"
src_val_images = "/media/arhan-erguven/Data/labels/val"
src_test_images = "/media/arhan-erguven/Data/labels/test"

dest_train_images = "/media/arhan-erguven/Data/images"
dest_val_images = "/media/arhan-erguven/Data/labels_new/val"
dest_test_images = "/media/arhan-erguven/Data/labels_new/test"

flatten_directory(src_train_images, dest_train_images)





