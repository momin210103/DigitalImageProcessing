from PIL import Image

# Step 1: Load and convert to grayscale
image_path =r'D:/ImageProcessing/images/ffgh.jpg'
img = Image.open(image_path).convert("L")
pixels = list(img.getdata())
width, height = img.size

# Step 2: Set a threshold (0–255)
threshold = 128  # change as needed

# Step 3: Apply threshold manually
binary_pixels = []
for p in pixels:
    if p >= threshold:
        binary_pixels.append(255)  # White
    else:
        binary_pixels.append(0)    # Black

# Step 4: Create and save binary image
binary_img = Image.new("L", (width, height))
binary_img.putdata(binary_pixels)
binary_img.save("binary_image.jpg")

# Optional: Show images
img.show(title="Original Grayscale")
binary_img.show(title="Binary Image")