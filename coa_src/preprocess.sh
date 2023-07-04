cur_dir=$(pwd)
export PYTHONPATH=${cur_dir}/DRS_parsing/:${PYTHONPATH}
export PYTHONPATH=${cur_dir}/DRS_parsing/evaluation/:${PYTHONPATH}

function preprocess() {
    lang=$1
    div=$2
    split=$3

    python src/preprocess.py \
        -i data/${lang}/${div}/${split}.txt \
        -v rel -r word -cd .tgt --drss_only
    while IFS= read -r line1 && IFS= read -r line2 <&3; do   echo -e "${line1}\t${line2}"; done < data/${lang}/${div}/${split}.txt.raw.tok 3< data/${lang}/${div}/${split}.txt.tgt > data/${lang}/${div}/${split}.alp
}

for lang in "en" "de"; do
    for split in "train" "dev" "test"; do
        preprocess $lang "gold" $split
    done
    preprocess $lang "gold_silver" "train"
done
preprocess "de" "gold_silver_bronze" "train"

for lang in "it" "nl"; do
    for split in "dev" "test"; do
        preprocess $lang "gold" $split
    done
    preprocess $lang "silver" "train"
    preprocess $lang "silver_bronze" "train"
done
