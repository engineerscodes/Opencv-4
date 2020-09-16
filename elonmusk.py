import cv2

img=cv2.imread('venv\image\dpelonmask.jpeg')
img=cv2.resize(img,(400,400))
cv2.imshow("git image",img)
cv2.imwrite('venv\image\git.jpeg',img)
cv2.waitKey(0)

cv2.destroyAllWindows()