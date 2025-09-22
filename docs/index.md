---
title: OpenNMT Indonesia ↔ Bima
description: Dokumentasi resmi OpenNMT untuk translasi Bahasa Indonesia ↔ Bima. Dibuat oleh HazelDev.
author: HazelDev
lang: id
---

# Indo-Bima Translation Model 🌐

Selamat datang di dokumentasi **Proyek Terjemahan Bahasa Indonesia ↔ Bahasa Bima**.

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
