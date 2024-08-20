from ultralytics import YOLO

model = YOLO("./runs/detect/train3/weights/epoch20.pt")

results = model.val(data = "test.yaml", imgsz= 640, batch=27)