import cv2
import numpy as np

video = cv2.VideoCapture("video6.mp4")

while True:
    ret, orig_frame = video.read()

    if not ret:
        video = cv2.VideoCapture("video6.mp4")
        continue

    frame = cv2.GaussianBlur(orig_frame, (5,5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_white = np.array([0, 0, 180])
    upper_white = np.array([180, 60, 255])
    mask = cv2.inRange(hsv, lower_white, upper_white)

    edges = cv2.Canny(mask, 75, 150)

    height, width = mask.shape
    roi = np.array([[
        (0, height),
        (0, int(height * 0.6)),
        (width, int(height * 0.6)),
        (width, height)
    ]], dtype=np.int32)

    roi_mask = np.zeros_like(mask)
    cv2.fillPoly(roi_mask, roi, 255)
    roi_edges = cv2.bitwise_and(edges, roi_mask)

    lines = cv2.HoughLinesP(roi_edges, 1, np.pi / 180, threshold=50, minLineLength=30, maxLineGap=30)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]

            angle = np.degrees(np.arctan2(y2 - y1, x2 - x1))
            if 20 < abs(angle) < 160:  
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 4)

    cv2.imshow("frame", frame)
    cv2.imshow("edges", roi_edges)

    key = cv2.waitKey(25)
    if key == 27 or key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
