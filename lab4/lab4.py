import cv2
import numpy as np
import matplotlib.pyplot as plt 

#load image in grey-scale
img = cv2.imread("lab4/container.jpg",cv2.IMREAD_GRAYSCALE)
#show image

# print(img.shape)

img = img[70:574,790:1200]

ret, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imshow('container',th1)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("crop-threshold.jpg", img)
    cv2.destroyAllWindows()