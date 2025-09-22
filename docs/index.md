---
title: "OpenNMT Indonesia ↔ Bima"
description: "Dokumentasi resmi proyek OpenNMT untuk translasi Bahasa Indonesia ↔ Bima. Dibuat oleh HazelDev."
author: "HazelDev"
layout: default
---

# 🌐 OpenNMT Indonesia ↔ Bima

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
