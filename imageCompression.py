# This program compresses an image using Singular Value Decomposition (SVD) and displays the original and compressed images side by side.

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

# Load the image and convert to grayscale
image = Image.open('image.jpg').convert('L')  # Replace 'example.jpg' with your image file path
image_array = np.array(image)

# Perform Singular Value Decomposition (SVD)
U, S, VT = np.linalg.svd(image_array, full_matrices=False)

# Keep only the top k singular values (adjustable for compression level)
k = input("Enter the number of singular values to keep: ")
k = int(k)
compressed_image = np.dot(U[:, :k] * S[:k], VT[:k, :])

# Save the compressed image temporarily to calculate its size
compressed_image_path = 'compressed_image_temp.jpg'
Image.fromarray(compressed_image.astype(np.uint8)).save(compressed_image_path)

# Get file sizes
original_file_size = os.path.getsize('image.jpg')
compressed_file_size = os.path.getsize(compressed_image_path)

# Clean up temporary file
os.remove(compressed_image_path)

# Display original and compressed images
#plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.title(f"Original Image\n{original_file_size / 1024:.2f} KB")
plt.imshow(image_array, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title(f"Compressed Image (k={k})\n{compressed_file_size / 1024:.2f} KB")
plt.imshow(compressed_image, cmap='gray')
plt.axis('off')

plt.show()
