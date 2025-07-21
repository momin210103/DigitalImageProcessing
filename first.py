import cv2
import numpy as np

#Read Image

img = cv2.imread("images/ffgh.jpg")
# print(type(img))
# print(img.shape)
# img_gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("window",img_gray)

img[:,:,2] =0

cv2.imshow("window",img)
cv2.waitKey(0)