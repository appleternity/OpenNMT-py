#!/bin/sh
source /home/czh5679/anaconda3/etc/profile.d/conda.sh
conda activate openNMT-scicap

data_folder="data/scicap-small"
image_folder="${data_folder}/image"

CUDA_VISIBLE_DEVICES="1" onmt_train -model_type img \
           -data ${data_folder}/demo \
           -save_model scicap_model \
           -gpu_ranks 0 \
           -batch_size 4 \
           -max_grad_norm 1.0 \
           -word_vec_size 256 \
           -encoder_type brnn \
           -decoder_type rnn \
           -dec_layers 4 \
           -enc_layers 4 \
           -dec_rnn_size 256 \
           -enc_rnn_size 256 \
           -rnn_type "LSTM" \
           -image_channel_size 3 \
           -save_checkpoint_steps 5000 \
           -valid_steps 5000 \
           -train_steps 50000 \
           -dropout 0.3 \
           -learning_rate 0.0001 \
           -start_decay_steps 10000 \
           -warmup_steps 4000 \

