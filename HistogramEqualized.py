import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images/Image1.jpg",cv2.IMREAD_GRAYSCALE)

rows ,cols = img.shape
total_pxl = rows*cols

#step 1: calculate hist
hist = np.zeros(256,dtype=int)
for i in range(rows):
    for j in range(cols):
        hist[img[i,j]] +=1

#step 2: calculate pdf
pdf = hist/total_pxl

#step 3: calculate cdf
cdf = np.cumsum(pdf)

#step 5: Normalize CDF 0 -255
equalized_map = np.round(cdf*255)

#step 6: Old pixels map to new pixels
equalized_img = np.zeros_like(img)
for i in range(rows):
    for j in range(cols):
        equalized_img[i,j] = equalized_map[img[i,j]]
#step 7: equalized histo
hist_eq = np.zeros(256,dtype=int)
for i in range(rows):
    for j in range(cols):
        hist_eq[equalized_img[i,j]] +=1


#plot

plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
plt.imshow(img,cmap='gray')
plt.title("Orginal Image")

plt.subplot(2,2,2)
plt.imshow(equalized_img,cmap='gray')
plt.title("New Image")

plt.subplot(2,2,3)
plt.bar(range(256),pdf,color='gray')
plt.title("Histogram")

plt.subplot(2,2,4)
plt.bar(range(256),hist_eq,color='gray')
plt.title("Equalized Histogram")
plt.tight_layout()
plt.show()
