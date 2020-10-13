import argparse
from cv2 import *

arg=argparse.ArgumentParser()
arg.add_argument("--input",help="enter video path",default=0)
args=vars(arg.parse_args())
cap=VideoCapture(args["input"])

while True:
    reg,frame=cap.read()
    if reg ==False:
        break
    cv2.imshow("OUPUT IMAGE",frame)
    if cv2.waitKey(100) & 0xFF==ord('q'):
        break
cap.release()
destroyAllWindows()