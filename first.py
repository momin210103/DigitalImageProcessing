import cv2
import numpy as np
import matplotlib.pyplot as plt

path=r'D:/ImageProcessing/images/ffgh.jpg'
img=cv2.imread(path,cv2.IMREAD_GRAYSCALE)
print("Image Shape: ",img.shape)

#gray level over 100
over_100_intensity=np.sum(img>100)
print(f'Pixels with gray level over 100 : {over_100_intensity}')

#maximum intensity in given picture
max_intensity=np.max(img)
print(f'Maximum gray level value {max_intensity}')

#replacing central value with mean of 3x3 neighbourhood window (helps smoothing the picture)
h,w=img.shape
center_y, center_x=h//2,w//2
neighborhood=img[center_y-1:center_y+2, center_x-1:center_x+2]
avg_value=int(np.mean(neighborhood))
img[center_y,center_x]=avg_value
print(f'Replacing values at {center_y}, {center_x} with neighbour window mean {avg_value}')

plt.imshow(img,cmap='gray')
plt.title('Modified Image')
plt.axis('off')
plt.show()


cv2.imwrite(r'C:\Users\monta\Downloads\Modified Map 2.jpg', img)


