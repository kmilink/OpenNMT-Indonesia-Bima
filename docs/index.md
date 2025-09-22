---
title: "OpenNMT Indonesia ↔ Bima"
description: "Dokumentasi resmi proyek OpenNMT untuk translasi Bahasa Indonesia ↔ Bima. Dibuat oleh HazelDev."
author: "HazelDev"
layout: default
---

<<<<<<< HEAD
# 🌐 OpenNMT Indonesia ↔ Bima
=======
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
>>>>>>> 0ac0ad308249fde150a2ebddd3865f8eb4adcf9e

Selamat datang di dokumentasi **Proyek Terjemahan Bahasa Indonesia ↔ Bahasa Bima**.  
Proyek ini bertujuan untuk melestarikan bahasa daerah Bima melalui teknologi **Neural Machine Translation (NMT)** berbasis **OpenNMT**.

---

## 🎯 Tujuan
Bahasa Bima adalah salah satu bahasa daerah di Indonesia yang perlu dilestarikan.  
Dengan adanya model terjemahan ini, diharapkan bahasa Bima dapat semakin dikenal dan digunakan di era digital.

---

## 📦 Teknologi
- **OpenNMT-py v1** → framework NMT.  
- **SentencePiece** → tokenisasi berbasis subword.  
- **Python 3.8+**.

---

## 📊 Dataset
Dataset terdiri dari pasangan kalimat **Indonesia ↔ Bima**.  
Saat ini tersedia lebih dari **5000+ pasangan kalimat** dan terus bertambah.

---

## 🚀 Cara Menjalankan

```bash
# 1. Clone repository
git clone https://github.com/HazelnutDev/OpenNMT-Indonesia-Bima.git
cd OpenNMT-Indonesia-Bima

# 2. Preprocessing
onmt_preprocess -config config/config.yaml

# 3. Training
onmt_train -config config/config.yaml

# 4. Inference (uji terjemahan)
onmt_translate -model models/model_step_xx.pt -src data/src-test.txt -output pred.txt
```

📌 Panduan lebih lengkap ada di file `tutorial.md`.

---

## 📖 Lisensi
Perangkat Lunak ini bersifat **Non-Komersial** dan mewajibkan atribusi kepada `HazelDev`.  
Lihat [LICENSE](LICENSE) untuk detail lengkap.  

---

Hak Cipta © 2025 HazelDev
