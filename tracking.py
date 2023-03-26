import cv2

cap = cv2.VideoCapture("ds1.mp4")


while True:
    _, frame = cap.read()
    images = cv2.resize(frame,(1280,720))
    cv2.imshow("frame",images)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()