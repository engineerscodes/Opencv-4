from cv2 import *;
import matplotlib.pyplot as plt
img=imread("C:\\Users\\HP\\PycharmProjects\\Image_processing\\venv\\image\\Elon-Musk-2010.jpg")
print(img.shape) #1600=colum and 1342 is rows and channels is 3
img_gray=imread('C:\\Users\\HP\\PycharmProjects\\Image_processing\\venv\\image\\Elon-Musk-2010.jpg',IMREAD_GRAYSCALE)
print(img_gray.shape) #1600=colum and 1342 is rows and channels is 0 because of grayScale image.
img_hsv=imread("C:\\Users\\HP\\PycharmProjects\\Image_processing\\venv\\image\\Elon-Musk-2010.jpg",COLOR_RGB2HSV)
print(img_hsv.shape) #the size (336,400) changes but channel is 3 output is (400,336,3)(rol=336,col=400)
print(img.dtype)
print(img_gray.dtype)
print(img_hsv.dtype) #all r unit 8 image
img=cv2.resize(img,(336,400)) # resizing image because its to big(1600,1342)
img_gray=resize(img_gray,(336,400))  #(y,x)
#img_gray[50:100,100:200]=1; altering pixel value of grayscale img.
imshow("Image of Elon Musk",img)
waitKey(100)
#destroyAllWindows()  if u remove this the windows will gwt destroyed after 100 mili second
imshow("Grayscale image of Musk",img_gray)
waitKey(100)
#destroyAllWindows()
imshow("HSV IMAGE OF ELON MUSK  ",img_hsv)

waitKey(0)  #it will not destroy img,img_hsv windows after 100 mili sec and its destroy when u press any key due to waitkey(0)
destroyAllWindows()