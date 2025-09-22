import pandas as pd

# === Konfigurasi ===
input_file = "corpus-fix.xlsx"        # ganti dengan nama file Excel kamu
output_file = "corpus_finalV2.xlsx"  # hasil disimpan di sini
col_src = "Indonesia"  # header kolom A
col_tgt = "Bima"       # header kolom B

# === Load data ===
df = pd.read_excel(input_file)

# Pastikan hanya ambil kolom yg dibutuhkan
df = df[[col_src, col_tgt]].copy()

# Hitung panjang kalimat (berdasarkan jumlah kata di kolom Indonesia)
df["len_src"] = df[col_src].astype(str).str.split().str.len()

# Urutkan dari panjang → pendek
df_sorted = df.sort_values(by="len_src", ascending=False).reset_index(drop=True)

# Hapus kolom bantu
df_sorted = df_sorted[[col_src, col_tgt]]

# Simpan hasil ke Excel baru
df_sorted.to_excel(output_file, index=False)

print(f"Data berhasil diurutkan dan disimpan ke {output_file}")
