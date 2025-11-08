import cv2
import numpy as np

img1 = cv2.imread("images/Image1.jpg")
img2 = cv2.imread("images/Image2.jpg")

img1 = cv2.resize(img1,(400,400))
img2 = cv2.resize(img2,(400,400))

rows,cols,ch = img1.shape
result = np.zeros((rows, cols, ch), dtype=np.uint8)

#Adition

for i in range(rows):
    for j in range(cols):
        for k in range(ch):
            b = int(img2[i,j,k])
            if b==0:
                b=1
            val = (int(img1[i, j, k]) / b)*255
            if val > 255:
                val = 255
            result[i,j,k]= val

cv2.imshow("Addition",result)
cv2.waitKey(0)
