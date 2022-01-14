import cv2
vd = cv2.VideoCapture(0)
while True:
    ret,frame = vd.read()
    cv2.imshow('nghia',frame)
    if cv2.waitKey(1) == ord('x'):
        break
vd.release()
cv2.destroyWindow()