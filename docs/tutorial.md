# Tutorial OpenNMT-py Versi 1.2

buka folder sentecepiece nya pak terus salin foldernya taroh difolder C langsung terus salin path nya terutama bin dll pada isi folder tersebut taro pada envirotmen variabel pada laptop dibagian system path baru jalankan semua kode atau script ini makasih😊

# 1. gabungkan file train sumber & target untuk training SPM
cat C:/Users/HazelDev/Desktop/OpenNMT-py/train.id-full.txt C:/Users/HazelDev/Desktop/OpenNMT-py/train.bhp-full.txt > C:/Users/HazelDev/Desktop/OpenNMT-py/all_for_sp.txt

## Asumsi total corpus atau dataset 7009 baris
head -n 6500 split-data/src.txt > train.id.txt 
head -n 6500 split-data/tgt.txt > train.bhp.txt
tail -n 509 split-data/src.txt | head -n 509 > valid.id.txt 
tail -n 509 split-data/tgt.txt | head -n 509 > valid.bhp.txt
## opsional
tail -n 100 split-data/src.txt | tail -n 100 > data/src-test.txt 
tail -n 100 split-data/tgt.txt | tail -n 100 > data/tgt-test.txt

# 2. create and training spm encode
# train sentencepiece (vocab 8000, tipe bpe recommended)
spm_train --input=C:/Users/HazelDev/Desktop/OpenNMT-py/all_for_sp.txt --model_prefix=C:/Users/HazelDev/Desktop/OpenNMT-py/onmt_data/spm --vocab_size=8000 --model_type=bpe --character_coverage=1.0

## encode bpe train
spm_encode --model=C:/Users/HazelDev/Desktop/OpenNMT-py/onmt_data/spm.model < C:/Users/HazelDev/Desktop/OpenNMT-py/train.id.txt  > C:/Users/HazelDev/Desktop/OpenNMT-py/data/train.id.spm
spm_encode --model=C:/Users/HazelDev/Desktop/OpenNMT-py/onmt_data/spm.model < C:/Users/HazelDev/Desktop/OpenNMT-py/train.bhp.txt  > C:/Users/HazelDev/Desktop/OpenNMT-py/data/train.bhp.spm

## encode bpe valid
spm_encode --model=C:/Users/HazelDev/Desktop/OpenNMT-py/onmt_data/spm.model < C:/Users/HazelDev/Desktop/OpenNMT-py/valid.id.txt  > C:/Users/HazelDev/Desktop/OpenNMT-py/data/valid.id.spm
spm_encode --model=C:/Users/HazelDev/Desktop/OpenNMT-py/onmt_data/spm.model < C:/Users/HazelDev/Desktop/OpenNMT-py/valid.bhp.txt  > C:/Users/HazelDev/Desktop/OpenNMT-py/data/valid.bhp.spm

# 3. prosesing onmt
onmt_preprocess \
  -train_src C:/Users/HazelDev/Desktop/OpenNMT-py/data/train.id.spm \
  -train_tgt C:/Users/HazelDev/Desktop/OpenNMT-py/data/train.bhp.spm \
  -valid_src C:/Users/HazelDev/Desktop/OpenNMT-py/data/valid.id.spm \
  -valid_tgt C:/Users/HazelDev/Desktop/OpenNMT-py/data/valid.bhp.spm \
  -save_data C:/Users/HazelDev/Desktop/OpenNMT-py/onmt_data \
  -src_seq_length 200 -tgt_seq_length 200 \
  -share_vocab

## jangan lupa pindahkan file onmt_data pada folder onmt_data biar supaya tidak ada kendala setelah menjalankan ini

# 4. Training onmt 
onmt_train \
  --data "C:/Users/HazelDev/Desktop/OpenNMT-py/onmt_data/onmt_data" \
  --save_model "C:/Users/HazelDev/Desktop/OpenNMT-py/model/bima" \
  --world_size 1 --gpu_ranks 0 \
  --model_type text \
  --encoder_type transformer --decoder_type transformer \
  --word_vec_size 256 --rnn_size 256 --transformer_ff 1024 --heads 4 \
  --enc_layers 4 --dec_layers 4 \
  --dropout 0.3 --attention_dropout 0.3 --position_encoding \
  --batch_type tokens --batch_size 3000 --accum_count 2 \
  --optim adam --learning_rate 2e-4 --warmup_steps 4000 \
  --label_smoothing 0.1 \
  --train_steps 5000 --valid_steps 500 --save_checkpoint_steps 500 \
  --model_dtype fp16 --early_stopping 3 --early_stopping_criteria ppl

# 5. inferensi atau coba test translate model
## inferensi supaya bisa dicek score bleu
onmt_translate \
  --model C:/Users/HazelDev/Desktop/OpenNMT-py/model/bima_step_5000.pt \
  --src C:/Users/HazelDev/Desktop/OpenNMT-py/data/test.id.spm \
  --output C:/Users/HazelDev/Desktop/OpenNMT-py/pred.bhp.spm \
  --gpu 0
  
## untuk cek inferensi akurat
onmt_translate \
  --model C:/Users/HazelDev/Desktop/OpenNMT-py/model/bima_step_5000.pt \
  --src C:/Users/HazelDev/Desktop/OpenNMT-py/data/test.id.spm \
  --output C:/Users/HazelDev/Desktop/OpenNMT-py/pred.bhp.spm \
  --gpu 0 \
  --batch_size 16 \
  --beam_size 5
  
# 6. decode atau merubah kembali isi file ke file yang mudah dibaca dari hasil translate
spm_decode.exe --model=onmt_data/spm.model --input=pred.bhp.spm --output=pred.bhp.txt

# 7. cek score bleu
cat C:/Users/HazelDev/Desktop/OpenNMT-py/pred.bhp.txt | sacrebleu C:/Users/HazelDev/Desktop/OpenNMT-py/data/test.bhp.txt
