# contoh (untuk referensi) -- aku sudah menjalankan versi ini untukmu
import pandas as pd
df = pd.read_excel("corpus-fix.xlsx")
df = df.iloc[:, :2]
df.columns = ["src","tgt"]
df["src"] = df["src"].astype(str).str.strip().str.replace(r"\s+"," ",regex=True).str.lower()
df["tgt"] = df["tgt"].astype(str).str.strip().str.replace(r"\s+"," ",regex=True).str.lower()
df = df.dropna().drop_duplicates()
# shuffle & split 90/10
