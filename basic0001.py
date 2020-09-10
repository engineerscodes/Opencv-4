from cv2 import *;

img=imread("C:\\Users\\HP\\PycharmProjects\\Image_processing\\venv\\image\\opencvlogo.png",1)
img_gray=imread("C:\\Users\\HP\\PycharmProjects\\Image_processing\\venv\\image\\opencvlogo.png",0)
img_hsv=imread("C:\\Users\\HP\\PycharmProjects\\Image_processing\\venv\\image\\opencvlogo.png",COLOR_BGR2HSV)
imshow("Colored images",img)
imshow("Gray Image",img_gray)
imshow("HSV Imege",img_hsv)
waitKey(0) #waits till you press any key
destroyAllWindows()
