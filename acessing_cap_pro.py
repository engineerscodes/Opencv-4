from cv2 import *
import argparse

arg=argparse.ArgumentParser()
arg.add_argument("--input",help='Video paths ',default=0)
args=vars(arg.parse_args())
cap=VideoCapture(args['input'])
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')) # depends on fourcc available camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(CAP_PROP_FPS,15)#still fps doesnot https://stackoverflow.com/questions/37442069/cap-prop-fps-doesnt-change-in-opencv-3
width=cap.get(CAP_PROP_FRAME_WIDTH)
heigth=cap.get(CAP_PROP_FRAME_HEIGHT)
FPS=cap.get(CAP_PROP_FPS)
print("frame width of video:'{}'".format(width))
print('frame heigth of video {}  \nFPS OF VIDEO :{}'.format(heigth,FPS))
index=0
while True:
    check,frame=cap.read()
    imshow("display",cvtColor(frame,COLOR_BGR2LAB))
    if waitKey(100) & 0xFF==ord('q'):
        break
    if waitKey(20) & 0xFF==ord('c'): #writing frame to local drive if 'c'is pressed,plz change the path to your drive
        file_name="C:\\Users\\HP\\PycharmProjects\\Image_processing\\venv\\image\\frame{}.jpg".format(index)
        index+=1
        imwrite(file_name,frame)
        #C:\Users\HP\PycharmProjects\Image_processing\venv\image

cap.release()
destroyAllWindows()