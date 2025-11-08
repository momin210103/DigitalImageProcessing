import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("images/ffgh.jpg",cv2.IMREAD_GRAYSCALE)

#---------mask-----#
mean_mask = [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
gauss_mask = [[1,2,1],[2,4,2],[1,2,1]]
lap_mask = [[0,-1,0],[-1,4,-1],[0,-1,0]]
sobel_x = [[-1,0,1],[-2,0,2],[-1,0,1]]
sobel_y = [[-1,-2,-1],[0,0,0],[1,2,1]]
prewitt_x = [[-1,0,1],[-1,0,1],[-1,0,1]]
prewitt_y = [[-1,-1,-1],[0,0,0],[1,1,1]]

r,c = img.shape
pad = 1
padded = np.pad(img.astype(int),((pad,pad),(pad,pad)),mode='constant', constant_values=0)


#---------Mean Filter---------#
mean_img = np.zeros_like(img)
for i in range(r):
    for j in range(c):
        s = 0
        for x in range(3):
            for y in range(3):
                s += padded[i+x,j+y] * mean_mask[x][y]
            mean_img[i,j] = s//9
#--------Gaussian Filter-------------#
gauss_img = np.zeros_like(img)
for i in range(r):
    for j in range(c):
        s = 0
        for x in range(3):
            for y in range(3):
                s += padded[i+x,j+y] * gauss_mask[x][y]
            gauss_img[i,j] = s // 16
#-----------Laplacian-----------#
lap_img = np.zeros_like(img)
for i in range(r):
    for j in range(c):
        s = 0
        for x in range(3):
            for y in range(3):
                s += padded[i+x,j+y] * lap_mask[x][y]
            val = abs(s)
            if val < 0: val =0
            if val > 255: val = 255
            lap_img[i,j] = val

#------------Sobel-------------#
sobel_img = np.zeros_like(img)
for i in range(r):
    for j in range(c):
        gx = 0
        gy = 0
        for x in range(3):
            for y in range(3):
                gx += padded[i+x,j+y] * sobel_x[x][y]
                gy += padded[i+x,j+y] * sobel_y[x][y]
        val = int ((gx**2 + gy**2)**0.5)
        if val > 255 : val = 255
        sobel_img[i,j] = val
# ----------------- Prewitt Filter -----------------
prewitt_img = np.zeros_like(img)
for i in range(r):
    for j in range(c):
        gx = 0
        gy = 0
        for x in range(3):
            for y in range(3):
                gx += padded[i+x,j+y]*prewitt_x[x][y]
                gy += padded[i+x,j+y]*prewitt_y[x][y]
        val = int((gx**2 + gy**2)**0.5)
        if val>255: val=255
        prewitt_img[i,j] = val

#-----------Display-------------#
titles = ['Original','Mean Filter','Gaussian Filter','Laplacian','Sobel','Prewitt']
images = [img,mean_img,gauss_img,lap_img,sobel_img,prewitt_img]


plt.figure(figsize=(12,8))
for i in range(6):
    plt.subplot(3,2,i+1)
    plt.imshow(images[i],cmap='gray')
    plt.title(titles[i])
    plt.axis('Off')
plt.tight_layout()
plt.show()