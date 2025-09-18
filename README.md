# Image Compression using Singular Value Decomposition (SVD)

This project demonstrates how **Singular Value Decomposition (SVD)** can be used to compress images while preserving essential visual features. The program takes an input image, applies SVD, and reconstructs a compressed version by keeping only the top `k` singular values. The original and compressed images are displayed side by side with their file sizes for comparison.

---

## What is SVD?

Singular Value Decomposition (SVD) is a matrix factorization technique in linear algebra:

$$
A = U \cdot S \cdot V^T
$$

* **U** and **V** are orthogonal matrices.
* **S** is a diagonal matrix containing singular values sorted in decreasing order.

In image compression, the largest singular values capture most of the important structure, while smaller ones represent fine details. By keeping only the top `k` singular values, we can approximate the original image with reduced storage requirements.

---

## How It Works

1. Load an image and convert it to grayscale.
2. Apply **SVD decomposition** to the image matrix.
3. Keep only the **top k singular values** (user-defined).
4. Reconstruct the compressed image using the reduced matrices.
5. Compare the **original and compressed images** side by side, including their file sizes.

---

## Example Usage

```bash
python svd_compression.py
```

* Input: `image.jpg`
* User prompt: Enter `k` (number of singular values to keep).
* Output:

  * Original image with size in KB
  * Compressed image with reduced size
  * Visual comparison of quality vs compression

---

## Tools & Libraries

* **Python 3**
* **NumPy** – numerical computations and SVD
* **Pillow (PIL)** – image loading and saving
* **Matplotlib** – image visualization


Do you want me to make this README **shorter and beginner-friendly**, or keep it in this **slightly technical format**?
