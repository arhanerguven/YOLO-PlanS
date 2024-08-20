import cv2

#img_path = "/media/arhan-erguven/Data/TrainSimulation/images (old)/0000001131_0000000000/0000001131_0000000000_0000000047.jpg"
img_path = "/media/arhan-erguven/Data/YOLO_TrainR/0000000056_0000000000/0000000056_0000000000_0000000082.jpg"
#label_path = "/media/arhan-erguven/Data/YOLO_Data_Final/0000001131_0000000000/0000001131_0000000000_0000000047.txt"
label_path = "/media/arhan-erguven/Data/YOLO_TrainR/0000000056_0000000000/0000000056_0000000000_0000000082.txt"

img = cv2.imread(img_path)
with open(label_path, "r") as f:
    for line in f:
        data = line.strip().split(" ")

        x = int(float(data[1])*640)
        y = int(float(data[2])*480)
        w = int(float(data[3])*640)
        h = int(float(data[4])*480)

        top_left_x = int(float(data[1])*640 - (float(data[3])*640)/2)
        top_left_y = int(float(data[2])*480 + (float(data[4])*480)/2)
        bottom_right_x = int(float(data[1])*640 + (float(data[3])*640)/2)
        bottom_right_y = int(float(data[2])*480 - (float(data[4])*480)/2)
        img = cv2.rectangle(img, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), color = (255,255,0))
        (w, h), _ = cv2.getTextSize(
            data[0], cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)


        # For printing text
        img = cv2.putText(img, data[0], (top_left_x, top_left_y+20),
                          cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

        #img = cv2.rectangle(img, (x,y), (x + w, y + h), color=(255,255,0))

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()