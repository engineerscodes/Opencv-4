'''from cv2 import *
import argparse
import pafy
arg=argparse.ArgumentParser()
arg.add_argument("-input",help="IP CAMERA URL",default='https://www.youtube.com/watch?v=_4rndwJWiSE')
args=vars(arg.parse_args())
url='https://www.youtube.com/watch?v=_4rndwJWiSE'
vPafy = pafy.new(url)
play = vPafy.getbest(preftype="webm")

cap=VideoCapture(play.url)
while True:
    check,frame=cap.read()
    imshow("output",frame)
    if waitKey(100) & 0xFF==ord('q'):
        break


cap.release()
destroyAllWindows()'''