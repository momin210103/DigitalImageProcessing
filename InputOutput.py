import cv2
import matplotlib.pyplot as plt
import numpy as np

path =r'D:/ImageProcessing/images/ffgh.jpg'
img = cv2.imread(path)
gray  = cv2.cvtColor(img,cv2.IMREAD_GRAYSCALE)

min_val = np.min(gray)
max_val = np.max(gray)
mean_val = np.mean(gray)

print(min_val)
print(max_val)
print(mean_val)


plt.imshow(gray)
plt.show()