# English & German
for lang in "en" "de";
    for split in "train" "dev" "test"; do
        cp data/exp_data_3.0.0/de/$lang/$split.txt data/$lang/gold/
    done
    cp data/exp_data_3.0.0/$lang/silver/train.txt data/$lang/gold_silver/silver_train.txt
    cat data/$lang/gold/train.txt > data/$lang/gold_silver/train.txt
    cat data/$lang/gold_silver/silver_train.txt >> data/$lang/gold_silver/train.txt
    rm data/$lang/gold_silver/silver_train.txt
done
cp data/exp_data_3.0.0/de/bronze/train.txt data/de/gold_silver_bronze/bronze_train.txt
cat data/de/gold_silver/train.txt > data/de/gold_silver_bronze/train.txt
cat data/de/gold_silver_bronze/bronze_train.txt >> data/de/gold_silver_bronze/train.txt
rm data/de/gold_silver_bronze/bronze_train.txt

# Italian & Dutch
for lang in "it" "nl"; do
    for split in "dev" "test"; do
        cp data/exp_data_3.0.0/$lang/gold/$split.txt data/$lang/gold/
    done
    cp data/exp_data_3.0.0/$lang/silver/train.txt data/$lang/silver/
    cp data/exp_data_3.0.0/$lang/bronze/train.txt data/$lang/silver_bronze/bronze_train.txt
    cat data/$lang/silver/train.txt > data/$lang/silver_bronze/train.txt
    cat data/$lang/silver_bronze/bronze_train.txt >> data/$lang/silver_bronze/train.txt
    rm data/$lang/silver_bronze/bronze_train.txt
done
