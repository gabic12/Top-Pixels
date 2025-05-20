import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

IMAGE_NAME = "dots.jpg"
NUMBER_OF_COLORS = 10
SQUARE_SIZE = 125  # Size of each color square in pixels

# Open the image and transform it into an array
image = Image.open("dots.jpg")
image_array = np.array(image)

# Ready the canvas
plt.figure(figsize=(10, 5))
plt.imshow(image_array)
plt.title("Image")
plt.axis("off")

# Reshape the image array into a 2D array and create a tuple of (R, G, B) for each pixel
pixels = image_array.reshape(-1, image_array.shape[-1])
pixel_tuples = [tuple(pixel) for pixel in pixels]

# Count the unique pixels and sort them
unique_pixels, pixel_count = np.unique(pixel_tuples, axis=0, return_counts=True)
sorted_pixels = np.argsort(-pixel_count)

top_pixels = unique_pixels[sorted_pixels[:NUMBER_OF_COLORS]]
top_counts = pixel_count[sorted_pixels[:NUMBER_OF_COLORS]]

for i in range(NUMBER_OF_COLORS):
    print(f"{i+1}: Pixel RGB {tuple(top_pixels[i])[0]},{tuple(top_pixels[i])[1]},{tuple(top_pixels[i])[2]} - Count: {top_counts[i]}")

# Create a new image
colors_image = Image.new("RGB", (SQUARE_SIZE * NUMBER_OF_COLORS, SQUARE_SIZE))
draw = ImageDraw.Draw(colors_image)

# For each pixel it will draw a square with the size of {SQUARE_SIZE} pixels
for i, color in enumerate(top_pixels):
    x_start = i * SQUARE_SIZE
    x_end = x_start + SQUARE_SIZE
    draw.rectangle([x_start, 0, x_end, SQUARE_SIZE], fill=tuple(color)) # Draw the squares side by side horizontally

# Display the images
colors_image.show()
plt.show()