import cv2
import os



mother_path = "/media/arhan-erguven/Data/YOLO_TestR"
dest_path = "/media/arhan-erguven/Data/YOLO_TestVis"

for folder_name in os.listdir(mother_path):
    dest_folder = os.path.join(dest_path, folder_name)
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)
    folder_inside = os.path.join(mother_path, folder_name)
    for file_name in os.listdir(folder_inside):
        file_path = os.path.join(folder_inside, file_name)
        if file_name.endswith(".txt"):
            img_path = file_path.replace(".txt", ".jpg")
            img = cv2.imread(img_path)
            with open(file_path, "r") as f:
                for line in f:
                    data = line.strip().split(" ")

                    top_left_x = int(float(data[1])*640 - (float(data[3])*640)/2)
                    top_left_y = int(float(data[2])*480 + (float(data[4])*480)/2)
                    bottom_right_x = int(float(data[1])*640 + (float(data[3])*640)/2)
                    bottom_right_y = int(float(data[2])*480 - (float(data[4])*480)/2)
                    img = cv2.rectangle(img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), color = (255,255,0))

                    (w, h), _ = cv2.getTextSize(
                        data[0], cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)

                    # For printing text
                    img = cv2.putText(img, data[0], (top_left_x, top_left_y + 20),
                                      cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

                    img_name = file_name.replace(".txt", ".jpg")
                    cv2.imwrite(os.path.join(dest_folder, img_name), img)
