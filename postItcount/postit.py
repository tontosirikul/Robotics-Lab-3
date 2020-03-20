import cv2
import numpy as np 
from matplotlib import pyplot as plt

image = cv2.imread("OpenCV-inRange-Picker-master 2/depositphotos_77014377-stock-photo-cork-board-seven-pinned-post.jpg",cv2.IMREAD_COLOR)
rows, cols, chs = image.shape
scale_percent = 50
width = int(image.shape[1]*scale_percent/100)
height = int(image.shape[0]*scale_percent/100)
dsize = (width,height)
image = cv2.resize(image,dsize)
blur_image = cv2.GaussianBlur(image,(5,5),0)
hsv = cv2.cvtColor(blur_image, cv2.COLOR_BGR2HSV)

lower_pink = np.array([110,20,20])
upper_pink = np.array([180,255,255])
mask_pink = cv2.inRange(hsv,lower_pink,upper_pink)

lower_yellow = np.array([22,122,230])
upper_yellow = np.array([25,255,255])
mask_yellow = cv2.inRange(hsv,lower_yellow,upper_yellow)

lower_green = np.array([25,38,205])
upper_green = np.array([43,85,255])
mask_green = cv2.inRange(hsv,lower_green,upper_green)

lower_blue = np.array([64,29,167])
upper_blue = np.array([91,255,255])
mask_blue = cv2.inRange(hsv,lower_blue,upper_blue)

def getContourDraw(img,mask):
    count = 0
    _, contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area >1000:
         cv2.drawContours(img, contours, -1,(0,255,0),2)
         count += 1
    return img,count

def draw_text_on_image(img_draw, countpink, countyellow,countgreen,countblue):
    cv2.rectangle(img_draw, (0, 0), (500, 40), (0,0,0), -1)
    cv2.putText(img_draw,'Pink Count : ' + str(countpink), 
        (10,11),                  # bottomLeftCornerOfText
        cv2.FONT_HERSHEY_SIMPLEX, # font 
        0.5,                      # fontScale
        (0,255,255),            # fontColor
        2)                        # lineType
    cv2.putText(img_draw,'Yellow Count : ' + str(countyellow), 
        (150,11),                  # bottomLeftCornerOfText
        cv2.FONT_HERSHEY_SIMPLEX, # font 
        0.5,                      # fontScale
        (0,255,255),            # fontColor
        2)                        # lineType
    cv2.putText(img_draw,'Green Count : ' + str(countgreen), 
        (10,30),                  # bottomLeftCornerOfText
        cv2.FONT_HERSHEY_SIMPLEX, # font 
        0.5,                      # fontScale
        (0,255,255),            # fontColor
        2)                        # lineType
    cv2.putText(img_draw,'Blue Count : ' + str(countblue), 
        (150,30),                  # bottomLeftCornerOfText
        cv2.FONT_HERSHEY_SIMPLEX, # font 
        0.5,                      # fontScale
        (0,255,255),            # fontColor
        2)                        # lineType
    return img_draw

image_draw,count_pink=getContourDraw(image,mask_pink)
image_draw,count_yellow=getContourDraw(image,mask_yellow)
image_draw,count_green=getContourDraw(image,mask_green)
image_draw,count_blue=getContourDraw(image,mask_blue)
draw_text_on_image(image_draw, count_pink, count_yellow,count_green,count_blue)
cv2.imwrite("result.jpg", image) 
cv2.imshow("Result",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

    



