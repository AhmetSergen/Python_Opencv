import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.png')

kernel = np.ones((5,5),np.float32)/25 #kernel matrix
dst = cv2.filter2D(img,-1,kernel)

#short methods for different techniques:
#blur = cv2.blur(img,(5,5))
#blur = cv2.GaussianBlur(img,(5,5),0)
#median = cv2.medianBlur(img,5)
#blur = cv2.bilateralFilter(img,9,75,75)

#plt.subplot(row,column,index)
plt.subplot(1,2,1),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()