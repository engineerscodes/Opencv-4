'''
@author -M.NAVEEN
RANDOM CODER'S
'''
import cv2
import numpy as np
face_cascade=cv2.CascadeClassifier("C:\\Users\\HP\\Documents\\python\\haarcascade_frontalface_default.xml")
img=cv2.imread("../../Documents/python/images.jpg", 1)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


faces1=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=10)
for x,y,w,h in faces1 :
                 img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)

for x,y,w,h in faces1:
                 img2=cv2.rectangle(gray_img,(x,y),(x+w,y+h),(0,255,0),5)
cv2.imshow("COLORED", img)
cv2.imshow("GRAY",img2)
# dectecting faces of different faces.
cv2.waitKey(0)

cv2.destroyAllWindows()
                                   


