# 🌐 OpenNMT Indonesia ↔ Bima

Proyek ini menyediakan **model penerjemahan otomatis (NMT)** untuk Bahasa **Indonesia ↔ Bima**, dibangun menggunakan **OpenNMT-py v1**.

## 🚀 Fitur
- Translasi otomatis Indonesia ↔ Bima.
- Dataset 5000+ pasangan kalimat.
- Dukungan penuh SentencePiece.
- Open source & gratis untuk riset.

## 📦 Teknologi
- Python 3.8+
- OpenNMT-py v1
- SentencePiece

## 📖 Dokumentasi
Lihat dokumentasi lengkap di [GitHub Pages](https://hazelnutdev.github.io/OpenNMT-Indonesia-Bima/).

## 🛠️ Cara Menjalankan
```bash
git clone https://github.com/HazelnutDev/OpenNMT-Indonesia-Bima.git
cd OpenNMT-Indonesia-Bima

onmt_preprocess -config config/config.yaml
onmt_train -config config/config.yaml
onmt_translate -model models/model_step_xx.pt -src data/src-test.txt -output pred.txt
```

## 📜 Lisensi
Lisensi **Non-Komersial** dengan atribusi wajib kepada HazelDev.
