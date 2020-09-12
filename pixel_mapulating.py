from cv2 import *
img=imread("C:\\Users\\HP\\PycharmProjects\\Image_processing\\venv\image\\elon_musk_tesla_3036.jpg")
#opencv by default is BGR
img=resize(img,(400,336))
(b,g,r)=img[45,45]
print(b,g,r)
#getting specific channel
g=img[335,399,1] #(y,x)
print(g)
imshow("ORIGINAL ELON MUSK PIC",img)
img[45:100,45:100]=(255,255,255)
imshow("ALTERED ELON MUSK PIC",img)
gray=cvtColor(img,COLOR_BGR2GRAY)
imshow("ALTERED ELON MUSK PIC in Grayscale",gray)
waitKey(0)

destroyAllWindows()