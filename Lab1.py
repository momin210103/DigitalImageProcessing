from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure

img_path  = r'D:/ImageProcessing/images/ffgh.jpg'
img = Image.open(img_path).convert('L')
img_arr = np.array(img)

#Negative Image
L = 256
neg_img = L - 1 - img_arr

#Log Transform
# s = c * log(1+r)

c = 255 /np.log(1+np.max(img_arr))
log_img = c * np.log(1+img_arr)



#Power_law
# s = c * r ^ y

gamma = 2.5
c = 255 / (np.max(img_arr) ** gamma)
gamma_img = c * (img_arr ** gamma)
#Contrast Stretching

r_min ,r_max = np.min(img_arr),np.max(img_arr)
stretch_img = ((img_arr-r_min)/(r_max-r_min)) * 255

#GrayLevel Slicing
a, b = 100, 180  # Range to highlight

# Without background suppression
slice1 = np.where((img_arr >= a) & (img_arr <= b), 255, img_arr)

# With background suppression
slice2 = np.where((img_arr >= a) & (img_arr <= b), 255, 0)


figure(figsize=(12,8))

plt.subplot(3,3,1)
plt.imshow(img, cmap='gray')
plt.title("Original")

plt.subplot(3,3,2)
plt.imshow(neg_img, cmap='gray')
plt.title("Negative")

plt.subplot(3,3,3)
plt.imshow(log_img,cmap='gray')
plt.title("Log Image")

plt.subplot(3,3,4)
plt.imshow(gamma_img,cmap='gray')
plt.title("Power_Law Image")

plt.subplot(3,3,5)
plt.imshow(stretch_img,cmap='gray')
plt.title("Stretch Image")

plt.subplot(3,3,6)
plt.imshow(slice1,cmap='gray')
plt.title("Gray Level Slicing Without background suppression")

plt.subplot(3,3,7)
plt.imshow(slice2,cmap='gray')
plt.title("Gray Level Slicing Without background suppression")


plt.tight_layout()
plt.show()