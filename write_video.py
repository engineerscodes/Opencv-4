from cv2 import *

cap=VideoCapture(0)
'''cap.set(CAP_PROP_FRAME_WIDTH,500)
cap.set(CAP_PROP_FRAME_HEIGHT,500)'''
fourcc=VideoWriter_fourcc('X','V','I','D') #fourcc of mp4 is  0x7634706d
gray=VideoWriter('naveen.avi',fourcc,int(30),(1020,1020),False)
while True:
    check,frame=cap.read()
    if check is True:
        back=cvtColor(frame,COLOR_BGR2GRAY)
        back=cv2.resize(back, (1020,1020))#VideoWriter('naveen.avi',fourcc,int(30),(1020,1020),False) both frame size and video cap size must be same
        imshow("video",back)
        gray.write(back)
        if waitKey(100) & 0xFF==ord('q'):
            break

gray.release()
cap.release()
destroyAllWindows()

