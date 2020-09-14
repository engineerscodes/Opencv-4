import argparse
from cv2 import *
import numpy as np
arg=argparse.ArgumentParser()
arg.add_argument("--path",help="INPUT VIDEO PATH ",default=0)
args=vars(arg.parse_args())

cap=cv2.VideoCapture(args['path'])
while (True):
    check,frame=cap.read()
    gray=cvtColor(frame,COLOR_RGB2GRAY)
    img_brg=cvtColor(frame,COLOR_RGB2BGR)
    img_hsv=cvtColor(frame,COLOR_BGR2HSV)
    imshow("displaying GRAY IMAGE -->",gray)
    imshow("displaying IMAGE -->",frame)
    imshow("displaying BRG IMAGE -->", img_brg)
    imshow("displaying HSV IMAGE -->", img_hsv)
    if waitKey(100) & 0xFF==ord('q'):
        break;
cap.release()
destroyAllWindows()
