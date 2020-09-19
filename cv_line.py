from cv2 import *
from color_dict import *
import  numpy as np
import matplotlib.pyplot as plt

img=np.zeros((400,400,3),dtype='uint8')
color=colors()
img[:]=color['white']

img=line(img,(0,0),(400,400),color['green'],10)
img=line(img,(0,400),(400,0),color['red'],10)
img=line(img,(200,0),(200,400),color['yellow'],10)
img=line(img,(0,200),(400,200),color['magenta'],10)
plt.imshow(img) #in MATHPLOTLIB red=blue ,opencv(RGB),MATPLOITLIB USES BGR
imshow('display',img)
plt.show()
waitKey(0)
destroyAllWindows()

