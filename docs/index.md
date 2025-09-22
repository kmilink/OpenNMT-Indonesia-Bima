# OpenNMT Indonesia ↔ Bima Translation

> 🔗 Akses penuh repository: [HazelnutDev/OpenNMT-Indonesia-Bima](https://github.com/HazelnutDev/OpenNMT-Indonesia-Bima)

## Tentang Proyek
Proyek ini bertujuan membangun **model terjemahan mesin** dari Bahasa Indonesia ke Bahasa Bima (dan sebaliknya) menggunakan framework **[OpenNMT-py](https://opennmt.net/OpenNMT-py/)**.  

Fokus utama proyek adalah:
- Mempreservasi bahasa daerah Bima melalui teknologi NLP.  
- Menyediakan dataset paralel Indonesia ↔ Bima.  
- Menghadirkan model yang dapat dijalankan secara lokal.  

## Teknologi yang Digunakan
- **Python 3.8+**  
- **OpenNMT-py v1** (stabil, berbasis CLI)  
- **SentencePiece** (untuk subword tokenization)  
- **PyTorch** sebagai backend  

## Dataset
Dataset terdiri dari pasangan kalimat **Indonesia ↔ Bima**, dikumpulkan dan disusun secara manual agar sesuai format OpenNMT.  

Struktur data:
```
data/
  ├── src-train.txt   # Kalimat sumber (Indonesia)
  ├── tgt-train.txt   # Kalimat target (Bima)
  ├── src-valid.txt   # Validasi sumber
  └── tgt-valid.txt   # Validasi target
```

## Cara Menjalankan
Untuk panduan instalasi, training, dan inferensi model, silakan lihat:  
📖 [Tutorial Lengkap](tutorial.md)

---

✍️ *Proyek ini masih dalam tahap pengembangan, kontribusi terbuka untuk siapa saja yang ingin mendukung pelestarian bahasa Bima melalui teknologi AI.*
