import pandas as pd

# Load file Excel
file_path = "Dataset.xlsx"   # ganti dengan path file kamu
df = pd.read_excel(file_path)

# Ubah semua isi dataframe menjadi lowercase
df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

# Simpan hasil ke file baru
output_path = "Dataset_final.xlsx"
df.to_excel(output_path, index=False)

print("File berhasil disimpan:", output_path)
