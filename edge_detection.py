import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.png',0)
edges = cv2.Canny(img,100,300)
#First argument is our input image. 
#Second and third arguments are our minVal and maxVal respectively. 
#Third argument is aperture_size. It is the size of Sobel kernel used for find image gradients. By default it is 3.

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()