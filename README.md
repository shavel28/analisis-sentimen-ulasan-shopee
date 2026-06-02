# 🛒 Analisis Sentimen Ulasan Pengguna Shopee Menggunakan Deep Learning

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk melakukan analisis sentimen terhadap ulasan pengguna aplikasi Shopee yang diperoleh dari Google Play Store. Analisis dilakukan menggunakan metode Deep Learning untuk mengklasifikasikan sentimen ulasan ke dalam kategori negatif, netral, dan positif.

Melalui proses preprocessing teks dan pelatihan model deep learning, proyek ini membantu memahami opini pengguna terhadap aplikasi Shopee berdasarkan ulasan yang diberikan.

---

## 📂 Dataset

Dataset diperoleh melalui proses scraping ulasan aplikasi Shopee menggunakan Google Play Scraper.

Data yang digunakan terdiri dari:

- Content (isi ulasan)
- Score (rating pengguna)

---

## 🏷️ Kategori Sentimen

| Rating | Sentimen |
|----------|----------|
| 1 - 2 | Negatif |
| 3 | Netral |
| 4 - 5 | Positif |

---

## ⚙️ Teknologi dan Library

- Python
- TensorFlow
- Keras
- Pandas
- NumPy
- NLTK
- Sastrawi
- Google Play Scraper
- Matplotlib

---

## 🔄 Tahapan Proyek

1. Pengambilan Data (Scraping)
2. Pembersihan Data
3. Pelabelan Sentimen
4. Text Preprocessing
5. Tokenizing dan Padding
6. Label Encoding
7. Split Data Training dan Testing
8. Early Stopping
9. Pelatihan Model Deep Learning
10. Evaluasi Model
11. Analisis Hasil

---

## 🧠 Model Deep Learning

Model yang digunakan dalam proyek ini:

- LSTM (Long Short-Term Memory)
- GRU (Gated Recurrent Unit)
- Dense Neural Network

---

## 📁 Struktur Repository

```text
├── dataset.csv
├── SCRAPING.py
├── SHAVA_Analisis_Sentimen_Ulasan_Shopee.ipynb
├── requirements.txt
└── README.md
```

---

## 🚀 Cara Menjalankan

### Clone Repository

```bash
git clone https://github.com/shavel28/analisis-sentimen-ulasan-shopee.git
```

### Install Dependensi

```bash
pip install -r requirements.txt
```

### Jalankan Notebook

```bash
jupyter notebook
```

Kemudian buka file:

```text
SHAVA_Analisis_Sentimen_Ulasan_Shopee.ipynb
```

---

## 🎯 Tujuan Pembelajaran

Proyek ini dibuat untuk mempelajari:

- Natural Language Processing (NLP)
- Text Preprocessing Bahasa Indonesia
- Deep Learning untuk Klasifikasi Teks
- Implementasi LSTM dan GRU
- Analisis Sentimen Ulasan Pengguna

---

## 👩‍💻 Penulis

**Shava Selvia Ramadhani S**

Mahasiswa Teknik Informatika  
Politeknik Negeri Jember

---

⭐ Jika repositori ini bermanfaat, jangan ragu untuk memberikan bintang pada repositori ini.
