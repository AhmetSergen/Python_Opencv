import cv2
import numpy as np

img = cv2.imread("lena.png")

#*# İmage shape
print (img.shape) #returns number of rows ,cols and channels

#*#value of pixel coordinated at 100x100
px = img[100,100]
print (px)

#*#accessing only blue pixel
blue = img[100,100,0]
print (blue)

#*#modify pixel value
#img[100,100] = [255,255,255]
#print img[100,100]

#*#modify pixel values
for x in range(0,512):
	for y in range(0,512):
		img.itemset((y,x,2),100) #0:blue , 1:green, 2:red
		#img.itemset((y,x,1),100)
		#img.itemset((y,x,0),100)
	
		#print (img[100,100]) #print values of pixel coordinated at 100x100

cv2.imwrite('lena_pixelvalue.png',img)

#*#modifying RED value
img.itemset((10,10,2),100) #modify
img.item(10,10,2) #print pixel's red value at 10x10 coordinates.

img[:,:,2] = 0 #set all reds to zero

#*# copy a specific area of image
#ball = img[280:340, 330:390]