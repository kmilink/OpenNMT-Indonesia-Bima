---
title: OpenNMT Indonesia ke Bima
---

# Model Translasi Bahasa Indonesia ↔ Bima berbasis OpenNMT (Neural Machine Translation)

## LANSUNG SAJA KE REPOSITORI GITHUB DIBAWAH INI :

🔗 Akses penuh repository: [HazelnutDev/OpenNMT-Indonesia-Bima](https://github.com/HazelnutDev/OpenNMT-Indonesia-Bima)

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
model/
  └── bima_step_5000.pt
onmt_data/
  ├── onmt_data.train.0.pt
  ├── onmt_data.valid.0.pt
  ├── onmt_data.vocab.pt
  ├── spm.model
  └── spm.vocab
split-data/
  ├── src.txt
  └── tgt.txt
sisa nya ikuti semua penempatan isi file sesuai pada github ini seperti:
  ├── train.id.txt (ini berisi source bahasa indonesia)
  ├── train.bhp.txt (ini berisi bahasa taregt Bima)
  ├── valid.id.txt (ini berisi source bahasa indonesia untuk validasi ketika training nanti)
  ├── valid.bhp.txt (ini berisi target bahasa Bima untuk validasi ketika training nanti)
  └── dan seterusnya samakan saja.
```

## Cara Menjalankan
Untuk panduan instalasi, training, dan inferensi model, silakan lihat:  
📖 [Tutorial Lengkap](tutorial.md)

---

✍️ *Proyek ini masih dalam tahap pengembangan, kontribusi terbuka untuk siapa saja yang ingin mendukung pelestarian bahasa Bima melalui teknologi AI.*
