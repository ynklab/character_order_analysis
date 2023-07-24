# Does Character-level Information Always Improve DRS-based Semantic Parsing?
Tomoya Kurosawa and Hitomi Yanaka

Appear in the 12th Joint Conference on Lexical and Computational Semantics (\*SEM 2023) with ACL 2023.


## Usage
### Directory setups
1. First of all, clone this repository.
```
git clone https://github.com/ynklab/character_order_analysis.git
```

2. Follow the setups on [Neural DRS parsing](https://github.com/RikVN/Neural_DRS/) and [AllenNLP experiments](https://github.com/RikVN/Neural_DRS/blob/master/AllenNLP.md) in the repository.
```
cd character_order_analysis
git clone https://github.com/RikVN/Neural_DRS.git

# setups for Neural_DRS
cd Neural_DRS
git clone https://github.com/RikVN/DRS_parsing.git
cd DRS_parsing
git checkout v.3.0.0
pip install -r requirements.txt
pip install scipy
pip install matplotlib
cd ..

# setups for AllenNLP experiments
git clone https://github.com/RikVN/allennlp
cd allennlp
git checkout DRS
pip install --editable .
cd ..
```

3. Copy directories in `character_order_analysis` into `Neural_DRS`. (the `coa_data` directory will be copied by `concat_data.sh`)
```
cp -r coa_config Neural_DRS/
cp -r coa_src Neural_DRS/
```

4. Download Parallel Meaning Bank (version 3.0.0) data for experiments.
Please install `exp_data_3.0.0.zip` from https://pmb.let.rug.nl/releases/, unzip and locate it in `data`.
```
cd data
wget https://pmb.let.rug.nl/releases/exp_data_3.0.0.zip
unzip exp_data_3.0.0.zip
```

### Data creation
1. Concat `pmb_exp_data_3.0.0` data in `data`.
```
./coa_src/concat_data.sh
```
2. Generate files for experiments followed [AllenNLP experiments](https://github.com/RikVN/Neural_DRS/blob/master/AllenNLP.md).
```
./coa_src/preprocess.sh
```
3. Generate files for experiments in our paper.
This script generates six character files for each div and split: normal (sent), shuffle.intoken, shuffle.inline, random, unify, and 2gram.
You can set n for ngrams as command line arguments. The default value is 2.
```
python coa_src/generate_char_file.py
```

### Run experiments
You have to set variables based on your required experiment.
```
./orig_src/run_experiment.sh $config_pretrain $config_finetune $save_dir
```

For example, if you want to run an experiment using normal character files, run below after setting `save_dir`.
```
./orig_src/run_experiment.sh config/en/common/pretrain.json config/en/common/finetune.json $save_dir
```

### Evaluation
We used DRS Jury.
See [DRS Jury](https://github.com/RikVN/Neural_DRS/blob/master/DRS_jury.md) for more detail.


## Citation
If you use our work in any published research, please cite the following:

Tomoya Kurosawa and Hitomi Yanaka. 2023. [Does Character-level Information Always Improve DRS-based Semantic Parsing?](https://arxiv.org/abs/2306.02302)
In *Proceedings of the 12th Joint Conference on Lexical and Computational Semantics (\*SEM 2023)*, Toronto, Ontario.
Association for Computational Linguistics.

```
@inproceedings{kurosawa-yanaka-2023-character,
    title = "Does Character-level Information Always Improve {DRS}-based Semantic Parsing?",
    author = "Kurosawa, Tomoya  and
      Yanaka, Hitomi",
    booktitle = "Proceedings of the The 12th Joint Conference on Lexical and Computational Semantics (*SEM 2023)",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.starsem-1.23",
    pages = "249--258",
    abstract = "Even in the era of massive language models, it has been suggested that character-level representations improve the performance of neural models. The state-of-the-art neural semantic parser for Discourse Representation Structures uses character-level representations, improving performance in the four languages (i.e., English, German, Dutch, and Italian) in the Parallel Meaning Bank dataset. However, how and why character-level information improves the parser{'}s performance remains unclear. This study provides an in-depth analysis of performance changes by order of character sequences. In the experiments, we compare F1-scores by shuffling the order and randomizing character sequences after testing the performance of character-level information. Our results indicate that incorporating character-level information does not improve the performance in English and German. In addition, we find that the parser is not sensitive to correct character order in Dutch. Nevertheless, performance improvements are observed when using character-level information.",
}

```


## Contact
For questions and usage issues, please contact kurosawa-tomoya@is.s.u-tokyo.ac.jp .


## License
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
