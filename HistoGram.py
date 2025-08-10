# Digital Image Processing - Manual Histogram Generation in Python
# No built-in histogram functions are used

from PIL import Image  # Only used for reading the image

# Step 1: Load image and convert to grayscale
image_path =r'D:/ImageProcessing/images/ffgh.jpg'  # Change to your image file
img = Image.open(image_path).convert("L")  # 'L' = grayscale

# Step 2: Get pixel values
pixels = list(img.getdata())  # Flat list of grayscale values (0–255)

# Step 3: Initialize histogram bins
hist = [0] * 256  # 256 bins for intensity levels

# Step 4: Count each pixel intensity
for p in pixels:
    hist[p] += 1

# Step 5: Display histogram as text
for intensity, count in enumerate(hist):
    print(f"Intensity {intensity:3}: {count}")

# Optional: Plot the histogram (for visualization in DIP course)
import matplotlib.pyplot as plt
plt.bar(range(256), hist, color='gray')
plt.title("Grayscale Histogram (Manual Calculation)")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.show()