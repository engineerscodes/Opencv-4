import numpy as np
import matplotlib.pyplot as plt
import color_dict as cd
from cv2 import *

color=cd.colors()
img=np.zeros((500,500,3),dtype="uint8")
img[:]=color['ligth_gray']
black_img=np.ones((500,500,3),dtype='uint8')#black image
white_img=np.zeros((500,500,3),dtype='uint8')#(h,w,no_of_channel)
white_img[:]=color['white']
seperation=40
for key in color:
    line(img,(0,seperation),(500,seperation),color[key],10)
    seperation+=40
img_con=np.concatenate((img,black_img,white_img),axis=1)
plt.imshow(img_con)
plt.show()
#imshow("dis",img)
cv2.waitKey(0)
destroyAllWindows()
