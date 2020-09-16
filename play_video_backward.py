from cv2 import *
import argparse

arg=argparse.ArgumentParser()
arg.add_argument("--input",help="INPUT PATH TO VIDEO FILE'S",default='C:\\Users\\HP\\Videos\\rename.m4v')
args=vars(arg.parse_args())
cap=VideoCapture(args['input'])

frame_count=cap.get(CAP_PROP_FRAME_COUNT)-1
'''cap.set(CAP_PROP_FRAME_WIDTH,400)
cap.set(CAP_PROP_FRAME_HEIGHT,400)'''
while True:
    print(cap.get(CAP_PROP_FPS))
    cap.set(CAP_PROP_POS_FRAMES,frame_count)
    check,frame=cap.read()
    frame=resize(frame,(400,400))
    imshow("FRAME OUTPUT-",frame)
    if waitKey(100) & 0xFF==ord('q'):
        break
    frame_count=frame_count-1
cap.release()
destroyAllWindows()




