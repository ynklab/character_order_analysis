# English & German
for lang in "en" "de"; do
    mkdir -p data/$lang/gold/
    mkdir -p data/$lang/gold_silver/
    for split in "train" "dev" "test"; do
        cp data/pmb_exp_data_3.0.0/$lang/gold/$split.txt data/$lang/gold/
    done
    cp data/pmb_exp_data_3.0.0/$lang/silver/train.txt data/$lang/gold_silver/silver_train.txt
    cat data/$lang/gold/train.txt > data/$lang/gold_silver/train.txt
    cat data/$lang/gold_silver/silver_train.txt >> data/$lang/gold_silver/train.txt
    rm data/$lang/gold_silver/silver_train.txt


done
mkdir -p data/$lang/gold_silver_bronze/
cp data/pmb_exp_data_3.0.0/de/bronze/train.txt data/de/gold_silver_bronze/bronze_train.txt
cat data/de/gold_silver/train.txt > data/de/gold_silver_bronze/train.txt
cat data/de/gold_silver_bronze/bronze_train.txt >> data/de/gold_silver_bronze/train.txt
rm data/de/gold_silver_bronze/bronze_train.txt

# Italian & Dutch
for lang in "it" "nl"; do
    mkdir -p data/$lang/gold/
    mkdir -p data/$lang/silver/
    mkdir -p data/$lang/silver_bronze/
    for split in "dev" "test"; do
        cp data/pmb_exp_data_3.0.0/$lang/gold/$split.txt data/$lang/gold/
    done
    cp data/pmb_exp_data_3.0.0/$lang/silver/train.txt data/$lang/silver/
    cp data/pmb_exp_data_3.0.0/$lang/bronze/train.txt data/$lang/silver_bronze/bronze_train.txt
    cat data/$lang/silver/train.txt > data/$lang/silver_bronze/train.txt
    cat data/$lang/silver_bronze/bronze_train.txt >> data/$lang/silver_bronze/train.txt
    rm data/$lang/silver_bronze/bronze_train.txt
done

for lang in "en" "de" "it" "nl"; do
    cp -r coa_data/$lang data/
done