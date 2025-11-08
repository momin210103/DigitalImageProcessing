import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images/Image1.jpg",cv2.IMREAD_GRAYSCALE)

rows ,cols = img.shape
result = np.zeros_like(img)
T = 127

for i in range(rows):
    for j in range(cols):
        if img[i,j] > T:
            result[i,j] = 255
        else:
            result[i,j] = 0

plt.figure(figsize=(12,8))
plt.subplot(1,2,1)
plt.imshow(img,cmap='gray')
plt.title("Orginal Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(result,cmap='gray')
plt.title("Binary Image")
plt.axis("off")
plt.show()
