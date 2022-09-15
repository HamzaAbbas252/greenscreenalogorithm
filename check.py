import cv2
import numpy as np

video = cv2.VideoCapture("gs.mp4")
img = cv2.imread("BG.jpg")
while True:
    ret , frame = video.read()
    frame=cv2.resize(frame,(900,600))
    img=cv2.resize(img,(900,600))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_range = np.array([45, 45, 70])
    upper_range = np.array([70, 255, 255])
    mask = cv2.inRange(hsv, lower_range, upper_range)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    f= frame-res
    f = np.where(f == 0, img, f)



    cv2.imshow("video",frame)
    cv2.imshow("Mask",f)


    if cv2.waitKey(1)==1:
        break

    #video.release()
    #cv2.destroyAllWindows()
