# tugascitra

**Nama                : Nadhia Shafira**

**Kelas               : I241E**

**Matkul              : Pengolahan Citra**

**Dosen Pengampu      : Dr. Muhamad Fatchan, S.Kom., M.Kom.**

---

# 📸 Deteksi Tepi Citra Digital: Sobel vs Canny
Tugas Praktikum Pertemuan 10 - Pengolahan Citra Digital

## 🛠️ Deskripsi Proyek
Proyek ini bertujuan untuk mengimplementasikan dan menganalisis metode deteksi tepi pada citra digital menggunakan dua algoritma populer: **Sobel** dan **Canny**. Analisis dilakukan secara mendalam mulai dari perhitungan manual (scratch), eksperimen parameter, hingga pembuatan aplikasi interaktif.

---

## 🔬 1. Implementasi Sobel (Manual vs OpenCV)
Pada tahap ini, dilakukan pembuatan fungsi konvolusi manual untuk menghitung gradien horizontal (Gx) dan vertikal (Gy).

### **Hasil Pengamatan Sobel:**
![Hasil Sobel](https://github.com/NadhiaShafira/tugascitra/blob/db25bd5ab6da78c52b5d6f5e5bd52ebc81acf873/sspengolahancitra/sobel_result.png)

**Analisis Data:**
* **Gx & Gy:** Menunjukkan arah perubahan intensitas. Gx mendeteksi garis vertikal, sedangkan Gy mendeteksi garis horizontal.
* **Magnitude:** Gabungan dari Gx dan Gy yang membentuk kerangka utuh dari sel darah.
* **Direction:** Peta warna menunjukkan sudut gradien di setiap piksel.
* **Akurasi (RMSE):** Berdasarkan hasil di terminal, didapatkan nilai **RMSE ≈ 0.000000**. 
  * *Interpretasi:* Hal ini membuktikan bahwa rumus konvolusi manual yang saya buat sudah 100% akurat dan identik dengan hasil library OpenCV.

---

## 🧬 2. Eksperimen Parameter Canny (Parameter Sweep)
Metode Canny lebih kompleks karena melibatkan Gaussian Blur dan Hysteresis Thresholding. Saya melakukan pengujian dengan variasi nilai **Sigma ($\sigma$)**, **Low Threshold**, dan **High Threshold**.

### **Hasil Pengamatan Canny:**
![Hasil Canny](./assets/canny_sweep.jpg)

**Analisis Data:**
1. **Pengaruh Sigma ($\sigma$):**
   * Semakin besar nilai Sigma, gambar semakin halus (blur). Ini sangat efektif untuk menghilangkan noise, tetapi jika terlalu besar, tepi sel darah yang tipis bisa hilang.
2. **Pengaruh Threshold (Low & High):**
   * **Low Threshold:** Mengontrol piksel mana yang dianggap sebagai "tepi lemah". Jika terlalu rendah, akan banyak bintik putih (noise) yang muncul.
   * **High Threshold:** Mengontrol "tepi kuat". Jika terlalu tinggi, struktur sel darah terlihat putus-putus.
3. **Kesimpulan:** Parameter terbaik untuk gambar sel darah adalah Sigma di kisaran 1.4 agar garis sel tetap menyambung namun tetap bersih dari noise.

---

## 💻 3. Aplikasi Web Deteksi Tepi (Streamlit)
Sebagai implementasi akhir, saya membuat aplikasi interaktif yang memungkinkan pengguna mencoba deteksi tepi pada berbagai jenis gambar secara real-time.

### **Hasil Pengamatan Web App:**
![Hasil Web App](./assets/webapp_result.jpg)

**Analisis Perbandingan (Sobel vs Canny):**
* **Kualitas Visual:** Canny menghasilkan garis yang jauh lebih tipis dan bersih (single-pixel edges) dibandingkan Sobel yang cenderung tebal.
* **Waktu Komputasi:** Berdasarkan statistik di aplikasi, **Sobel cenderung lebih cepat** karena tahapannya lebih sederhana. Canny membutuhkan waktu lebih lama karena harus melakukan proses Gaussian Blur dan penekanan non-maksimum.
* **Fleksibilitas:** Aplikasi ini berhasil memproses gambar bebas (foto natural) dengan baik, membuktikan bahwa algoritma ini adaptif untuk berbagai kondisi citra.

---

## 🚀 Cara Menjalankan
1. Clone repository ini.
2. Install library: `pip install opencv-python numpy matplotlib streamlit`.
3. Jalankan aplikasi:
   ```bash
   streamlit run tugas3_aplikasi_edge.py
