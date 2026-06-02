# Analisis Sentimen Ulasan Shopee

## Deskripsi Proyek
Proyek ini bertujuan untuk melakukan analisis sentimen terhadap ulasan pengguna aplikasi Shopee yang diperoleh dari Google Play Store. Analisis dilakukan menggunakan teknik Machine Learning untuk mengklasifikasikan sentimen pengguna menjadi positif, negatif, atau netral.

## Dataset
Dataset diperoleh melalui proses scraping ulasan aplikasi Shopee menggunakan library Google Play Scraper. Dataset berisi:
- Content (isi ulasan)
- Score (rating pengguna)

## Tahapan Proyek
1. Data Scraping
2. Data Cleaning
3. Preprocessing Text
4. Exploratory Data Analysis (EDA)
5. Pelabelan Sentimen
6. Feature Extraction
7. Training Model
8. Evaluasi Model

## Tools dan Library
- Python
- Pandas
- NumPy
- Scikit-Learn
- NLTK
- Sastrawi
- Google Play Scraper
- Matplotlib
- Seaborn

## Struktur Repository

├── dataset.csv  
├── SCRAPING.py  
├── SHAVA_Analisis_Sentimen_Ulasan_Shopee.ipynb  
├── requirements.txt  
└── README.md  

## Cara Menjalankan
1. Clone repository
```bash
git clone https://github.com/username/analisis-sentimen-ulasan-shopee.git
