from PIL import Image

# Step 1: Load and convert to grayscale

image_path =r'D:/ImageProcessing/images/ffgh.jpg'
img = Image.open(image_path).convert("L")
pixels = list(img.getdata())
width, height = img.size
total_pixels = width * height

# Step 2: Compute histogram manually
hist = [0] * 256
for p in pixels:
    hist[p] += 1

# Step 3: Compute normalized CDF (Cumulative Distribution Function)
cdf = [0] * 256
cdf[0] = hist[0]
for i in range(1, 256):
    cdf[i] = cdf[i-1] + hist[i]

# Step 4: Normalize CDF to map to [0, 255]
cdf_min = min(c for c in cdf if c > 0)  # smallest non-zero CDF value
cdf_normalized = [
    round((cdf[i] - cdf_min) / (total_pixels - cdf_min) * 255)
    for i in range(256)
]

# Step 5: Map original pixels to equalized values
equalized_pixels = [cdf_normalized[p] for p in pixels]

# Step 6: Create and save equalized image
equalized_img = Image.new("L", (width, height))
equalized_img.putdata(equalized_pixels)
equalized_img.save("histogram_equalized.jpg")

# Optional: Show before and after
img.show(title="Original Image")
equalized_img.show(title="Histogram Equalized Image")