from cv2 import *

cap=VideoCapture(0)
cap.set(CAP_PROP_FRAME_WIDTH,500)
cap.set(CAP_PROP_FRAME_HEIGHT,500)
fourcc=VideoWriter_fourcc('M','P','4','V') #fourcc of mp4 is  0x7634706d
gray=VideoWriter('naveen.mp4',0x7634706d,int(30),(500,500),False)
while True:
    check,frame=cap.read()
    if check is True:
        back=cvtColor(frame,COLOR_BGR2GRAY)
        imshow("video",back)
        gray.write(back)
        if waitKey(100) & 0xFF==ord('q'):
            break

gray.release()
cap.release()
destroyAllWindows()

