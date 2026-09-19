from ultralytics import YOLO
import cv2

model = YOLO('../Yolo-Weights/yolov8l.pt')
results = model("Images/1.png")
annotated_img = results[0].plot()  # Get the annotated image

cv2.imshow("Detection", annotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()