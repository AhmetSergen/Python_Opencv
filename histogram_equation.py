import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('lena.png',0)

#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))

cv2.imwrite('res.png', res)

plt.hist(img.ravel(),256,[0,256])
plt.show()

plt.hist(equ.ravel(),256,[0,256])
plt.show()

# create a CLAHE object (Arguments are optional).

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(3,3))
cl1 = clahe.apply(img)

cv2.imwrite('clahe_2.png',cl1)