# Does Character-level Information Always Improve DRS-based Semantic Parsing?
Tomoya Kurosawa and Hitomi Yanaka

Appear in the 12th Joint Conference on Lexical and Computational Semantics (\*SEM 2023) with ACL 2023.


## Usage
### Directory setups
* First of all, you have to follow the setups on [Neural DRS parsing](https://github.com/RikVN/Neural_DRS/) and [AllenNLP experiments](https://github.com/RikVN/Neural_DRS/blob/master/AllenNLP.md) in the repository.
* Then, you need Parallel Meaning Bank (version 3.0.0) data for experiments.
Please install `exp_data_3.0.0.zip` from [https://pmb.let.rug.nl/releases/], unzip and locate it in `data`.

### Data creation
1. Concat `exp_data_3.0.0` data in `data`.
```
./orig_src/concat_data.sh
```
2. Generate files for experiments followed [AllenNLP experiments](https://github.com/RikVN/Neural_DRS/blob/master/AllenNLP.md).
```
./orig_src/preprocess.sh
```
3. Generate files for experiments in our paper.
This script generates six character files for each div and split: normal (sent), shuffle.intoken, shuffle.inline, random, unify, and 2gram.
You can set n for ngrams as command line arguments. The default value is 2.
```
python orig_src/generate_char_file.py
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
See [DRS Jury](https://github.com/RikVN/Neural_DRS/blob/master/DRS_jury.md) by van Noord for more detail.


## Citation
If you use our work in any published research, please cite the following:

Tomoya Kurosawa and Hitomi Yanaka. 2023. [Does Character-level Information Always Improve DRS-based Semantic Parsing?](https://arxiv.org/abs/2306.02302)
In *Proceedings of the 12th Joint Conference on Lexical and Computational Semantics (\*SEM 2023)*, Toronto, Ontario.
Association for Computational Linguistics.

```
@Inproceedings{kurosawa-yanaka-2023-character,
    title = "Does Character-level Information Always Improve DRS-based Semantic Parsing?",
    author = "Kurosawa, Tomoya  and
      Yanaka, Hitomi",
    booktitle = "Proceedings of the 12th Joint Conference on Lexical and Computational Semantics",
    month = "jul",
    year = "2023",
    address = "Toronto, Ontario",
    publisher = "Association for Computational Linguistics",
}
```


## Contact
For questions and usage issues, please contact [kurosawa-tomoya@is.s.u-tokyo.ac.jp] .


## License
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
