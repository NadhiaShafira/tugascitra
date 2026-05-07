import cv2
import numpy as np
import matplotlib.pyplot as plt
from itertools import product

def canny_experiment(image_path):
    # 1. Load gambar dalam grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # 2. Tentukan variasi parameter sesuai instruksi modul
    sigmas = [0.5, 1.5]            # Variasi kehalusan (blur)
    low_thresholds = [30, 70]      # Ambang bawah
    high_thresholds = [100, 200]   # Ambang atas
    
    # Simpan hasil dalam list untuk diplot
    results = []
    params_label = []
    
    # Loop untuk mencoba semua kombinasi (Parameter Sweep)
    for sigma, low, high in product(sigmas, low_thresholds, high_thresholds):
        # Apply Gaussian Blur berdasarkan sigma
        ksize = int(6 * sigma + 1)
        if ksize % 2 == 0: ksize += 1
        blurred = cv2.GaussianBlur(img, (ksize, ksize), sigma)
        
        # Canny Detection
        edges = cv2.Canny(blurred, low, high)
        
        # Hitung jumlah piksel tepi untuk analisis kuantitatif
        edge_count = np.sum(edges > 0)
        
        results.append(edges)
        params_label.append(f"S={sigma}, L={low}, H={high}\nEdges: {edge_count}")

    # 3. Visualisasi Hasil Eksperimen
    plt.figure(figsize=(16, 10))
    for i in range(len(results)):
        plt.subplot(2, 4, i+1)
        plt.imshow(results[i], cmap='gray')
        plt.title(params_label[i], fontsize=9)
        plt.axis('off')
    
    plt.suptitle(f'Analisis Parameter Canny pada {image_path}', fontsize=16)
    plt.tight_layout()
    plt.show()

# Jalankan eksperimen untuk gambar sel_darah.jpeg
canny_experiment('sel_darah.jpeg')