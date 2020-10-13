import cv2
from pyzbar.pyzbar import decode
import argparse
import numpy as np
arg=argparse.ArgumentParser()
arg.add_argument("--input",help="enter video path ",default=0)
args=vars(arg.parse_args())
cap=cv2.VideoCapture(args["input"])

while cap.isOpened():
    reg,frame=cap.read()
    if reg == False:
        break
    #frame=cv2.GaussianBlur(frame,(5,5),0)
    #frame=cv2.medianBlur(frame,5)
    frame=cv2.bilateralFilter(frame,5,5,75)
    bar=decode(frame)

    for barcode in decode(frame):
        data=barcode.data.decode("utf-8")
        print(data)
        rect_pts=np.array([barcode.polygon],np.int32)
        rect_pts=rect_pts.reshape((-1,1,2))
        cv2.polylines(frame,[rect_pts],True,(255,0,255),5)
        pts=barcode.rect
        cv2.putText(frame,data,(pts[0],pts[1]),cv2.FONT_HERSHEY_TRIPLEX,1,(255,0,255),2)

    cv2.imshow("OUPUT IMAGE", frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

