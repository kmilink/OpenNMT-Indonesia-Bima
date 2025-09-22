import sentencepiece as spm

# Lokasi file
base = "C:/Users/HazelDev/Desktop/OpenNMT-py/"
input_file = base + "all_for_sp.txt"

# 1) Training SentencePiece model (BPE, vocab_size=8000)
spm.SentencePieceTrainer.Train(
    f"--input={input_file} --model_prefix={base}spm --vocab_size=8000 "
    f"--character_coverage=1.0 --model_type=bpe"
)

# 2) Load model yg barusan dibuat
sp = spm.SentencePieceProcessor()
sp.load(base + "spm.model")

# Helper function untuk encode file
def encode_file(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f_in, \
         open(output_path, "w", encoding="utf-8") as f_out:
        for line in f_in:
            pieces = sp.encode(line.strip(), out_type=str)
            f_out.write(" ".join(pieces) + "\n")

# 3) Encode semua file train/valid
encode_file(base + "train.id.txt",  base + "data/train.id.spm")
encode_file(base + "train.bhp.txt", base + "data/train.bhp.spm")
encode_file(base + "valid.id.txt",  base + "data/valid.id.spm")
encode_file(base + "valid.bhp.txt", base + "data/valid.bhp.spm")

print("✅ Selesai encode semua file dengan SentencePiece.")
