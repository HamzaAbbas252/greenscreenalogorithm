import cv2

video = cv2.VideoCapture("gs.mp4")

while True:

    ret , frame = video.read()
    frame=cv2.resize(frame,(480,680))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow("frame",frame)
    k=cv2.waitKey(1)
    if k == ord('q'):
        break
    video.release()
    cv2.destroyAllWindows()

