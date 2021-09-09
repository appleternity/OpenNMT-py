#!/bin/sh
source /home/czh5679/anaconda3/etc/profile.d/conda.sh
conda activate openNMT-scicap

data_folder="data/scicap-small"
#image_folder="/data01/tingyao/figure_caption/data/images"
image_folder="${data_folder}/image"

onmt_preprocess -data_type img \
                -src_dir ${image_folder} \
                -train_src ${data_folder}/src-train.txt \
                -train_tgt ${data_folder}/tgt-train.txt \
                -valid_src ${data_folder}/src-val.txt \
                -valid_tgt ${data_folder}/tgt-val.txt \
                -save_data ${data_folder}/demo \
                -tgt_seq_length 100 \
                -tgt_words_min_frequency 5 \
                -image_channel_size 3 \
                -overwrite
#                -shard_size 500 \
