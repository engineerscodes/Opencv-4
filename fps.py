from cv2 import *
import time
cap=VideoCapture(0)
width=cap.get(CAP_PROP_FRAME_WIDTH)
heigth=cap.get(CAP_PROP_FRAME_HEIGHT)
while cap.isOpened():
    check,frame=cap.read()

    if check is True:
      start_time = time.time_ns()
      gray =cvtColor(frame,COLOR_BGR2GRAY)
      putText(gray,'NAVEEN',(int (220),int (200)),FONT_ITALIC,fontScale=3,color=(255,255,255),thickness=10)
      imshow("Displaying Video",gray)
      end_time=time.time_ns()
      times=end_time-start_time
      try:
       print("FPS IS {}".format(1.0/times))
      except ZeroDivisionError :
          print("start times is equal to end")






      if waitKey(100) & 0xFF==ord('q'):
          break

cap.release()
destroyWindow("Displaying Video")

