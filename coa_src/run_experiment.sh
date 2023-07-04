#!/bin/bash

lang=$1
cmd=$2
exp_dir=$3

config_pretrain="config/$lang/$cmd/pretrain.json"
config_finetune="config/$lang/$cmd/finetune.json"

./src/allennlp_scripts/pipeline.sh $config_pretrain $exp_dir normal $lang 0
for i in 1 2 3; do
    ./src/allennlp_scripts/pipeline.sh $config_finetune $exp_dir finetune $lang $i
done
