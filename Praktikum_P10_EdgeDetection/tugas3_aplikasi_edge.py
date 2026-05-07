import streamlit as st
import cv2
import numpy as np
from PIL import Image
import time

# Konfigurasi Judul Halaman
st.set_page_config(page_title="Edge Detection App - Nadhia", layout="wide")
st.title("🔍 Aplikasi Deteksi Tepi: Sobel vs Canny")
st.write("Tugas Praktikum Pertemuan 10 - Pengolahan Citra Digital")

# --- SIDEBAR: KONTROL PARAMETER ---
st.sidebar.header("⚙️ Pengaturan Parameter")

# Pilih Metode
method = st.sidebar.selectbox("Pilih Metode Deteksi", ["Sobel", "Canny", "Bandingkan Keduanya"])

# Slider untuk Sobel
if method in ["Sobel", "Bandingkan Keduanya"]:
    st.sidebar.subheader("Parameter Sobel")
    s_ksize = st.sidebar.slider("Kernel Size (Ganjil)", 1, 7, 3, step=2)
    s_thresh = st.sidebar.slider("Threshold Sobel", 0, 255, 50)

# Slider untuk Canny
if method in ["Canny", "Bandingkan Keduanya"]:
    st.sidebar.subheader("Parameter Canny")
    c_sigma = st.sidebar.slider("Sigma (Gaussian Blur)", 0.1, 3.0, 1.4)
    c_low = st.sidebar.slider("Low Threshold", 0, 150, 50)
    c_high = st.sidebar.slider("High Threshold", 50, 300, 150)

# --- UPLOAD GAMBAR ---
file_up = st.file_uploader("Upload Gambar Kamu (JPG/PNG)", type=['jpg', 'jpeg', 'png'])

if file_up is not None:
    # Baca gambar
    image = Image.open(file_up)
    img_np = np.array(image)
    
    # Konversi ke Grayscale untuk pengolahan
    if len(img_np.shape) > 2:
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
    else:
        gray = img_np

    # Layout Kolom
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, caption="Gambar Asli", use_container_width=True)

    # --- EKSEKUSI METODE ---
    
    # JIKA PILIH SOBEL
    if method == "Sobel":
        t1 = time.perf_counter()
        gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=s_ksize)
        gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=s_ksize)
        mag = np.sqrt(gx**2 + gy**2)
        _, res_sobel = cv2.threshold(mag, s_thresh, 255, cv2.THRESH_BINARY)
        t2 = time.perf_counter()
        
        with col2:
            st.image(res_sobel.astype(np.uint8), caption="Hasil Sobel", use_container_width=True)
            st.info(f"Waktu Proses: {(t2-t1)*1000:.2f} ms")

    # JIKA PILIH CANNY
    elif method == "Canny":
        t1 = time.perf_counter()
        # Blur manual sesuai sigma
        k = int(6 * c_sigma + 1)
        if k % 2 == 0: k += 1
        blurred = cv2.GaussianBlur(gray, (k, k), c_sigma)
        res_canny = cv2.Canny(blurred, c_low, c_high)
        t2 = time.perf_counter()
        
        with col2:
            st.image(res_canny, caption="Hasil Canny", use_container_width=True)
            st.info(f"Waktu Proses: {(t2-t1)*1000:.2f} ms")

    # JIKA BANDINGKAN KEDUANYA
    else:
        st.divider()
        c1, c2 = st.columns(2)
        # Hitung Sobel
        s_mag = np.sqrt(cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=s_ksize)**2 + 
                        cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=s_ksize)**2)
        _, res_s = cv2.threshold(s_mag, s_thresh, 255, cv2.THRESH_BINARY)
        
        # Hitung Canny
        k = int(6 * c_sigma + 1)
        if k % 2 == 0: k += 1
        res_c = cv2.Canny(cv2.GaussianBlur(gray, (k, k), c_sigma), c_low, c_high)
        
        c1.image(res_s.astype(np.uint8), caption="Sobel", use_container_width=True)
        c2.image(res_c, caption="Canny", use_container_width=True)

else:
    st.warning("Silakan upload gambar dulu ya ka!")