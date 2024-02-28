import cv2
import numpy as np

# img = cv2.imread('lena.jpg',1)

#creating ur own image

img = np.zeros([512,512,3],np.uint8) #height,width,3 here is the number of colorchannels which is BGR then datatype

#image,point 1,point 2,colour(BGR),THICKNESS(-1 will fill)
img = cv2.line(img,(0,0),(255,255),(0,0,255),5)
img = cv2.circle(img,(0,255),255,(255,0,0),2)

#text 
font = cv2.FONT_HERSHEY_PLAIN
img = cv2.putText(img,"What's up?",(90,450),font,4.0,(0,255,0),5,cv2.LINE_AA)

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
