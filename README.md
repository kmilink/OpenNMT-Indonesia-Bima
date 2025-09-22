# Indo-Bima Translation Model

Proyek ini bertujuan untuk membangun model terjemahan mesin dari **Bahasa Indonesia ↔ Bahasa Bima** menggunakan [OpenNMT](https://opennmt.net/).  
Model ini dirancang untuk mendukung pelestarian bahasa daerah serta memperluas akses teknologi NLP untuk bahasa Bima.

## 🚀 Fitur
- Dataset paralel Indonesia ↔ Bima (5000+ pasangan kalimat, terus bertambah).
- Preprocessing menggunakan SentencePiece (tokenisasi subword).
- Training model berbasis [OpenNMT-py v1](https://github.com/OpenNMT/OpenNMT-py).
- Inferensi untuk uji coba translasi.

## 📂 Struktur Proyek
```
├── data/               # Dataset paralel (src, tgt, train, valid, test)
├── config/             # Konfigurasi OpenNMT
├── models/             # Model hasil training
├── LICENSE             # Lisensi proyek
├── README.md           # Dokumentasi proyek
└── index.md            # Dokumentasi untuk GitHub Pages
```

## ⚖️ Lisensi
Proyek ini menggunakan lisensi khusus berbasis MIT dengan ketentuan tambahan:
- **Non-Komersial** → Tidak boleh digunakan untuk tujuan komersial.
- **Atribusi Wajib** → Cantumkan nama `HazelDev` sebagai pencipta asli.
- **Larangan Penyalahgunaan** → Dilarang untuk tujuan ilegal atau merugikan.

Lihat berkas [LICENSE](LICENSE) untuk detail lengkap.

## 🌐 GitHub Pages
Dokumentasi dapat diakses melalui [GitHub Pages](https://hazelnutdev.github.io/OpenNMT-Indonesia-Bima/).

## 🤝 Kontribusi
Pull request dan kontribusi sangat terbuka!  
Silakan fork repo ini dan buat perubahan melalui PR.

---
Hak Cipta (c) 2025 HazelDev
