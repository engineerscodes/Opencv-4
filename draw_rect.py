from cv2 import *
from color_dict import *
import numpy as np
import matplotlib.pyplot as plt

color=colors()
img=np.zeros((500,500,3),dtype='uint8')
img[:]=color['white']
rectangle(img,(10,100),(130,300),color['red'],10)

cv2.imshow("display",img)
waitKey(0)
destroyAllWindows()