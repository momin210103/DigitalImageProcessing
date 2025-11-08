import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images/Image1.jpg",cv2.IMREAD_GRAYSCALE)

rows,cols = img.shape
total_pixels = rows * cols

#step 1: Calculate Histogram
hist = np.zeros(256,dtype=int)
for i in range(rows):
    for j in range(cols):
        hist[img[i,j]] +=1

#step2: calcuate pdf
pdf = hist/total_pixels

#show figure
plt.figure(figsize=(12,8))

plt.subplot(2,1,1)
plt.imshow(img,cmap='gray')
plt.title("orginal Image")

plt.subplot(2,1,2)
plt.bar(range(256),pdf,color='gray')
plt.title("Histogram")

plt.show()
