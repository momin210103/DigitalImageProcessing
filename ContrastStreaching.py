from PIL import Image

# Load and convert to grayscale
image_path =r'D:/ImageProcessing/images/ffgh.jpg'
img = Image.open(image_path).convert("L")
pixels = list(img.getdata())
width, height = img.size

# Step 1: Find min and max intensity
r_min = min(pixels)
r_max = max(pixels)

print(f"Original Min: {r_min}, Max: {r_max}")

# Step 2: Apply contrast stretching formula:
# new_pixel = (pixel - r_min) * (255 / (r_max - r_min))
stretched_pixels = []
for p in pixels:
    new_val = int((p - r_min) * (255 / (r_max - r_min)))
    # Clamp to 0–255 just in case
    new_val = max(0, min(255, new_val))
    stretched_pixels.append(new_val)

# Step 3: Create new image from stretched pixels
stretched_img = Image.new("L", (width, height))
stretched_img.putdata(stretched_pixels)
stretched_img.save("contrast_stretched.jpg")

# Optional: Show images
img.show(title="Original Image")
stretched_img.show(title="Contrast Stretched Image")