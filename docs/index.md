---
title: OpenNMT Indonesia ↔ Bima
description: Dokumentasi resmi OpenNMT untuk translasi Bahasa Indonesia ↔ Bima. Dibuat oleh HazelDev.
author: HazelDev
lang: id
---

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- SEO Meta Tags -->
  <title>OpenNMT Indonesia ↔ Bima | HazelNutDev</title>
  <meta name="description" content="Proyek OpenNMT Indonesia ↔ Bima. Model penerjemahan Neural Machine Translation (NMT) berbasis OpenNMT untuk bahasa Indonesia dan bahasa Bima.">
  <meta name="keywords" content="OpenNMT, Indonesia, Bima, Translation, Machine Learning, Neural Machine Translation, HazelNutDev">
  <meta name="author" content="HazelNutDev">

  <!-- Open Graph (biar bagus pas dibagi di sosial media) -->
  <meta property="og:title" content="OpenNMT Indonesia ↔ Bima | HazelNutDev">
  <meta property="og:description" content="Proyek OpenNMT untuk translasi bahasa Indonesia ↔ Bima. Gratis dan open source.">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://hazelnutdev.github.io/OpenNMT-Indonesia-Bima/">
  <meta property="og:image" content="https://hazelnutdev.github.io/OpenNMT-Indonesia-Bima/assets/cover.png">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="OpenNMT Indonesia ↔ Bima | HazelNutDev">
  <meta name="twitter:description" content="Proyek OpenNMT untuk translasi bahasa Indonesia ↔ Bima. Gratis dan open source.">
  <meta name="twitter:image" content="https://hazelnutdev.github.io/OpenNMT-Indonesia-Bima/assets/cover.png">

  <!-- Canonical URL -->
  <link rel="canonical" href="https://hazelnutdev.github.io/OpenNMT-Indonesia-Bima/">

  <!-- Favicon -->
  <link rel="icon" href="https://hazelnutdev.github.io/OpenNMT-Indonesia-Bima/assets/favicon.ico" type="image/x-icon">
</head>

# Indo-Bima Translation Model 🌐

Selamat datang di dokumentasi **Proyek Terjemahan Bahasa Indonesia ↔ Bahasa Bima**.

## Dokumentasi Lengkap dapat diakses melalui [GitHub Hazeldev](https://github.com/HazelnutDev/OpenNMT-Indonesia-Bima/?no-cache=1).

## 🎯 Tujuan
Bahasa Bima adalah salah satu bahasa daerah di Indonesia yang perlu dilestarikan.  
Dengan adanya model terjemahan ini, diharapkan bahasa Bima dapat semakin dikenal dan digunakan di era digital.

## 📦 Teknologi yang Digunakan
- **OpenNMT-py v1** → framework untuk Neural Machine Translation (NMT).
- **SentencePiece** → tokenisasi berbasis subword.
- **Python 3.8+**.

## 📊 Dataset
Dataset terdiri dari pasangan kalimat Indonesia ↔ Bima.  
Saat ini tersedia lebih dari **5000+ pasangan kalimat** yang terus ditambah.

## 🛠️ Cara Menjalankan
1. Clone repository ini:
   ```bash
   git clone https://github.com/HazelnutDev/Indo-Bima-Translate.git
   cd Indo-Bima-Translate
   ```
2. Siapkan data di folder `data/`.
3. Jalankan preprocessing:
   ```bash
   onmt_preprocess -config config/config.yaml
   ```
4. Mulai training:
   ```bash
   onmt_train -config config/config.yaml
   ```
5. Lakukan inferensi (uji terjemahan):
   ```bash
   onmt_translate -model models/model_step_xx.pt -src data/src-test.txt -output pred.txt
   ```
6. jika masih bingung langsung saja buka file tutorial yang sudah saya siapkan untuk memudahkan kalian untuk menjalankan semua perintah yang harus dijalankan supaya berjalan dengan baik dan sukses.

## 📖 Lisensi
Perangkat Lunak ini bersifat **Non-Komersial** dan mewajibkan atribusi kepada `HazelDev`.  
Lihat berkas [LICENSE](LICENSE) untuk informasi lebih lengkap.

---
Hak Cipta (c) 2025 HazelDev
