from cv2 import *
import argparse

arg=argparse.ArgumentParser()
arg.add_argument("--input",help='Video paths ',default=0)
args=vars(arg.parse_args())
cap=VideoCapture(args['input'])

width=cap.get(CAP_PROP_FRAME_WIDTH)
heigth=cap.get(CAP_PROP_FRAME_HEIGHT)
FPS=cap.get(CAP_PROP_FPS)
print("frame width of video:'{}'".format(width))
print('frame heigth of video {}  \nFPS OF VIDEO :{}'.format(heigth,FPS))
index=0
while True:
    check,frame=cap.read()
    imshow("display",frame)
    if waitKey(100) & 0xFF==ord('q'):
        break
    if waitKey(20) & 0xFF==ord('c'): #writing frame to local drive if 'c'is pressed,plz change the path to your drive
        file_name="C:\\Users\\HP\\PycharmProjects\\Image_processing\\venv\\image\\frame{}.jpg".format(index)
        index+=1
        imwrite(file_name,frame)
        #C:\Users\HP\PycharmProjects\Image_processing\venv\image

cap.release()
destroyAllWindows()