import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# --- 1. FUNGSI KONVOLUSI MANUAL (Dari Scratch) ---
def manual_convolution(image, kernel):
    # Padding Reflect agar ukuran output sama dengan input (sesuai modul)
    padded_img = np.pad(image, 1, mode='reflect')
    h, w = image.shape
    output = np.zeros((h, w), dtype=np.float64)
    
    for y in range(h):
        for x in range(w):
            # Ambil area 3x3
            region = padded_img[y:y+3, x:x+3]
            # Perkalian elemen-per-elemen dan dijumlahkan
            output[y, x] = np.sum(region * kernel)
    return output

# --- 2. IMPLEMENTASI SOBEL ---
def process_sobel(image_path):
    # Load gambar & konversi ke Grayscale
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float64)
    
    # Define Kernel Sobel Gx dan Gy
    Gx_kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    Gy_kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    
    # Hitung Gx dan Gy secara Manual
    gx_manual = manual_convolution(gray, Gx_kernel)
    gy_manual = manual_convolution(gray, Gy_kernel)
    
    # Hitung Magnitude & Arah Gradien (Tugas Poin 11-12)
    magnitude = np.sqrt(gx_manual**2 + gy_manual**2)
    # Arah dalam derajat
    direction = np.arctan2(gy_manual, gx_manual) * 180 / np.pi
    
    # Thresholding sederhana (Tugas Poin 13)
    _, thresholded = cv2.threshold(magnitude.astype(np.uint8), 50, 255, cv2.THRESH_BINARY)
    
    # --- 3. PEMBANDING OPENCV & RMSE (Tugas Poin 14-15) ---
    gx_cv = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    gy_cv = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    mag_cv = np.sqrt(gx_cv**2 + gy_cv**2)
    
    # Hitung RMSE (Root Mean Square Error)
    rmse = np.sqrt(np.mean((mag_cv - magnitude)**2))
    print(f"Hasil Perhitungan RMSE: {rmse:.6f}")
    
    return gray, gx_manual, gy_manual, magnitude, direction, thresholded

# --- RUN & VISUALISASI ---
IMAGE_FILE = 'sel_darah.jpeg'
gray, gx, gy, mag, direct, thresh = process_sobel(IMAGE_FILE)

# Menampilkan hasil sesuai urutan
plt.figure(figsize=(15, 10))

plt.subplot(231), plt.imshow(gray, cmap='gray'), plt.title('Original Gray')
plt.subplot(232), plt.imshow(np.abs(gx), cmap='gray'), plt.title('Gx (Horizontal)')
plt.subplot(233), plt.imshow(np.abs(gy), cmap='gray'), plt.title('Gy (Vertical)')
plt.subplot(234), plt.imshow(mag, cmap='gray'), plt.title('Magnitude')
plt.subplot(235), plt.imshow(direct, cmap='hsv'), plt.title('Direction (Map)')
plt.subplot(236), plt.imshow(thresh, cmap='gray'), plt.title('Thresholded (T=50)')

plt.tight_layout()
plt.show()