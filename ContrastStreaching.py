import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image in grayscale
img = cv2.imread("images/Image1.jpg", cv2.IMREAD_GRAYSCALE)

r_min = np.min(img)
r_max = np.max(img)

s = ((img - r_min) / (r_max - r_min)) * 255
s = s.astype(np.uint8)
# Show images
plt.figure(figsize=(12,6))
plt.subplot(1,2,1); plt.title("Original Image"); plt.imshow(img, cmap='gray'); plt.axis('off')
plt.subplot(1,2,2); plt.title("After Contrast Stretching"); plt.imshow(s, cmap='gray'); plt.axis('off')
plt.show()
