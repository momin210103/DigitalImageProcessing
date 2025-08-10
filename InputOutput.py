import cv2
import matplotlib.pyplot as plt

path =r'D:/ImageProcessing/images/ffgh.jpg'
img = cv2.imread(path)
img_rgb  = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


plt.imshow(img_rgb)
plt.show()