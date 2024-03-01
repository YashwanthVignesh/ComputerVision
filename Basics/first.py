import cv2
import numpy as np
print(cv2.__version__)
print(np.__version__)
# 1 color 0 grayscaṇle -1 alpha channel
img = cv2.imread('lena.jpg',-1)
print(img) #matrix of the image
cv2.imshow('image',img)
k = cv2.waitKey(0) #wait for 5s before closing
# 0 means it wont close until a keystroke is made
if( k==27 ):
    cv2.destroyAllWindows()
elif (k == ord('s')):
    cv2.imwrite('lena_copy.png',img)
    cv2.destroyAllWindows()
