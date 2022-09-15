import cv2
import numpy as np

video = cv2.VideoCapture("gs.mp4")
background= cv2.VideoCapture("v2.mp4")

while True:
    ret1 , frame1 = video.read()
    ret2 , frame2 = background.read()

    frame1=cv2.resize(frame1,(900,600))
    frame2=cv2.resize(frame2,(900,600))

    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    lower_range = np.array([45, 45, 70])
    upper_range = np.array([70, 255, 255])
    mask = cv2.inRange(hsv, lower_range, upper_range)
    res = cv2.bitwise_and(frame1, frame1, mask=mask)
    f= frame1-res
    f = np.where(f == 0, frame2, f)



    cv2.imshow("video",frame1)
    cv2.imshow("Mask",f)


    if cv2.waitKey(1)==1:
        break

    #video.release()
    #cv2.destroyAllWindows()
