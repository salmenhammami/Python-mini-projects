import cv2
import cvzone
from ultralytics import YOLO
import math
from SORT import *

cap = cv2.VideoCapture("video.mp4")
cap.set(3, 1280)  # Set width
cap.set(4, 720)   # Set height
model = YOLO('../Yolo-Weights/yolov8l.pt')

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
            "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
            "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
            "handbag" "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
            "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
            "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
            "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
            "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
            "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
            "teddy bear", "hair drier", "toothbrush"]
mask = cv2.imread("mask.png")

# Tracking :
tracker = Sort(max_age=30, min_hits=3, iou_threshold=0.3)
limits = [900, 850, 900, 350]
totalCount = []

while True:
    success, img = cap.read()
    imgRegion = cv2.bitwise_and(img, mask)
    results = model(imgRegion, stream=True)
    detections = np.empty((0, 5))
    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            # Confidence
            conf = math.ceil((box.conf[0] * 100))/100
            # Class Name
            cls=int(box.cls[0])
            currentClass = classNames[cls]
            if (currentClass == "car" or currentClass == "motorbike" or currentClass == "bus" or currentClass == "truck") and conf > 0.5:
                cvzone.putTextRect(img, f'{currentClass} {conf}', (max(0, x1), max(35, y1)),scale=1, thickness=1)
                cvzone.cornerRect(img, (x1, y1, x2-x1, y2-y1), l=10)
                currentArray = np.array([x1, y1, x2, y2, conf])
                detections = np.vstack((detections, currentArray)) 

    resultsTracker = tracker.update(detections)
    cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (255, 0, 255), 2)
    for res in resultsTracker:
        x1, y1, x2, y2, Id = res
        x1, y1, x2, y2, Id = int(x1), int(y1), int(x2), int(y2), int(Id)
        print(res)
        w, h =x2 - x1, y2 - y1
        # cvzone.putTextRect(img, f'ID: {Id}', (max(0, x1), max(35, y1)), scale=2, thickness=3, offset=10)
        # cvzone.cornerRect(img, (x1, y1, x2-x1, y2-y1), l=10, rt=2, colorR=(255, 0, 255))
        cx, cy = x1 + w // 2, y1 + h // 2
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        if limits[0] - 15 < cx < limits[0] + 15 and limits[3] < cy < limits[1] :
            if Id not in totalCount:
                totalCount.append(Id)
                cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255, 0), 5)

    cvzone.putTextRect(img, f'Count: {len(totalCount)}', (50, 50), scale=1, thickness=2, offset=10)
    cv2.imshow("Image", img)
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
