import cv2
import numpy as np

img = cv2.imread('lena.png')

#b, g, r = cv2.split(img)
red = cv2.equalizeHist(img[:,:,2]) 
green = cv2.equalizeHist(img[:,:,1])
blue = cv2.equalizeHist(img[:,:,0])
	
img_output=cv2.merge((blue, green, red))
	
cv2.imshow('Color input image', img)
cv2.imshow('Histogram equalized', img_output)

cv2.waitKey(0)	
	