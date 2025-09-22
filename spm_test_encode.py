import sentencepiece as spm

sp = spm.SentencePieceProcessor()
sp.load("C:/Users/HazelDev/Desktop/OpenNMT-py/onmt_data/spm.model")

# baca input
with open("C:/Users/HazelDev/Desktop/OpenNMT-py/data/test.id.txt", encoding="utf-8") as f:
    lines = [line.strip() for line in f]

# encode
with open("C:/Users/HazelDev/Desktop/OpenNMT-py/data/test.id.spm", "w", encoding="utf-8") as f:
    for line in lines:
        pieces = sp.encode(line, out_type=str)
        f.write(" ".join(pieces) + "\n")
