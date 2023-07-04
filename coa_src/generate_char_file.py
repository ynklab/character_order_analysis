import argparse
import random
random.seed(774)


LANGUAGES = ["en", "de", "it", "nl"]
DIV_SPLIT_DICT = {
    "en": [("gold", "train"), ("gold", "dev"), ("gold", "test"), ("gold_silver", "train")],
    "de": [
        ("gold_silver", "train"), ("gold", "dev"), ("gold", "test"),
        ("gold_silver_bronze", "train")],
    "it": [("silver", "train"), ("gold", "dev"), ("gold", "test"), ("silver_bronze", "train")],
    "nl": [("silver", "train"), ("gold", "dev"), ("gold", "test"), ("silver_bronze", "train")],
}

SPECIAL_SPACE = "|||"
SPECIAL_CAPITAL = "^^^"


def create_arg_parser():
    '''Create argument parser'''
    parser = argparse.ArgumentParser()
    # Parameter that are import to set
    parser.add_argument('-n', "--ngram", default=2, type=int, help="n of n-grams")

    return parser.parse_args()


def is_space(c):
    return c == " " or c == "~" or c == u'\xa0'


def sent_to_char(c):
    if is_space(c):
        return [SPECIAL_SPACE]
    elif c != c.lower():
        return [SPECIAL_CAPITAL, c.lower()]
    else:
        return [c]


def sent_to_chars(s):
    t = []
    for c in s:
        t += sent_to_char(c)
    return t


def func(s):
    t = []
    for c in s:
        if c == " " or c == "~":
            t.append("|||")
        elif c != c.lower():
            t.append("^^^")
            t.append(c.lower())
        else:
            t.append(c)
    return t


def shuffle(chars):
    ret = []
    while len(chars) > 0:
        rnd = random.randrange(len(chars))
        ret.append(chars[rnd])
        chars.pop(rnd)
    return ret


def shuffle_intoken(lang, div, split):
    in_file = f"data/{lang}/{div}/{split}.txt.raw.char.sent"
    out_file = f"data/{lang}/{div}/{split}.txt.raw.char.shuffle.intoken"
    with open(in_file, "r") as f:
        input_sents = [list(s.strip().split(' ')) for s in f.readlines()]

    output_sents = []
    for sent in input_sents:
        output_sent = []
        index = 0
        chars = []
        next_cap = False
        while index < len(sent):
            chars = []
            next_cap = False
            while index < len(sent) and sent[index] != SPECIAL_SPACE:
                if next_cap:
                    chars.append(sent[index].upper())
                    next_cap = False
                elif sent[index] == SPECIAL_CAPITAL:
                    next_cap = True
                else:
                    chars.append(sent[index])
                index += 1

            new_chars = shuffle(chars)
            for char in new_chars:
                if char != char.lower():
                    output_sent.append(SPECIAL_CAPITAL)
                    output_sent.append(char.lower())
                else:
                    output_sent.append(char)
            if index < len(sent):
                output_sent.append(SPECIAL_SPACE)
                index += 1
        output_sents.append(output_sent)

    with open(out_file, "w") as f:
        for sent in output_sents:
            print(' '.join(sent), file=f)


def shuffle_inline(lang, div, split):
    in_file = f"data/{lang}/{div}/{split}.txt.raw.char.sent"
    out_file = f"data/{lang}/{div}/{split}.txt.raw.char.shuffle.inline"
    with open(in_file, "r") as f:
        input_sents = [list(s.strip().split(' ')) for s in f.readlines()]

    output_sents = []
    for sent in input_sents:
        output_sents.append(shuffle(sent))

    with open(out_file, "w") as f:
        for sent in output_sents:
            print(' '.join(sent), file=f)


def gen_random(lang, div, split):
    in_file = f"data/{lang}/{div}/{split}.txt.raw.char.sent"
    out_file = f"data/{lang}/{div}/{split}.txt.raw.char.random"
    input_sents = []
    char_set = set()
    with open(in_file, "r") as f:
        for s in f.readlines():
            input_sents.append(list(s.strip().split(' ')))
            for c in input_sents[-1]:
                if len(c) == 3 or ord(c) not in [32, 160]:
                    char_set.add(c)
    char_list = list(char_set)

    output_sents = []
    for sent in input_sents:
        output_sent = []
        for _ in range(len(sent)):
            rnd = random.randrange(len(char_list))
            output_sent.append(char_list[rnd])
        output_sents.append(output_sent)

    with open(out_file, "w") as f:
        for sent in output_sents:
            print(' '.join(sent), file=f)


def unify(lang, div, split, unify_char='a'):
    in_file = f"data/{lang}/{div}/{split}.txt.raw.char.sent"
    out_file = f"data/{lang}/{div}/{split}.txt.raw.char.unify"
    with open(in_file, "r") as f:
        input_sents = [list(s.strip().split(' ')) for s in f.readlines()]

    output_sents = []
    for sent in input_sents:
        output_sent = [unify_char] * len(sent)
        output_sents.append(output_sent)

    with open(out_file, "w") as f:
        for sent in output_sents:
            print(' '.join(sent), file=f)


def ngram(lang, div, split, n=1):
    in_file = f"data/{lang}/{div}/{split}.txt.raw.tok"
    if n == 1:
        out_file = f"data/{lang}/{div}/{split}.txt.raw.char.sent"
    else:
        out_file = f"data/{lang}/{div}/{split}.txt.raw.char.{n}gram"
    with open(in_file, "r") as f:
        input_sents = [s.strip() for s in f.readlines()]

    output_sents = []
    for sent in input_sents:
        output_sent = []
        in_chars = sent_to_chars(sent)
        for i in range(len(in_chars) - n + 1):
            temp_chars = ""
            for j in range(n):
                temp_chars += in_chars[i + j]
            output_sent.append(temp_chars)
        output_sents.append(output_sent)

    with open(out_file, "w") as f:
        for sent in output_sents:
            print(' '.join(sent), file=f)


def unified_gold_silver(ext, lang):
    input_file = f"data/{lang}/gold_silver/train.txt.raw.char.{ext}"
    output_file = f"data/{lang}/gold/train.txt.raw.char.{ext}"
    with open(input_file, "r") as f:
        input_sents = [s.strip() for s in f.readlines()]
    with open(output_file, "r") as f:
        N = len([s.strip() for s in f.readlines()])
    with open(output_file, "w") as f:
        for i in range(N):
            print(input_sents[i], file=f)


def unified_gold_silver_bronze(ext, lang):
    input_file = f"data/{lang}/gold_silver_bronze/train.txt.raw.char.{ext}"

    output_file = f"data/{lang}/gold_silver/train.txt.raw.char.{ext}"
    with open(input_file, "r") as f:
        input_sents = [s.strip() for s in f.readlines()]
    N_gsb = len(input_sents)
    with open(output_file, "r") as f:
        N_gs = len([s.strip() for s in f.readlines()])
    with open(output_file, "w") as f:
        for i in range(N_gs):
            print(input_sents[i], file=f)

    """
    output_file = f"data/{lang}/gold/train.txt.raw.char.{ext}"
    with open(output_file, "r") as f:
        N_g = len([s.strip() for s in f.readlines()])
    with open(output_file, "w") as f:
        for i in range(N_g):
            print(input_sents[i], file=f)

    output_file = f"data/{lang}/silver_bronze/train.txt.raw.char.{ext}"
    with open(output_file, "w") as f:
        for i in range(N_g, N_gsb):
            print(input_sents[i], file=f)

    output_file = f"data/{lang}/silver/train.txt.raw.char.{ext}"
    with open(output_file, "w") as f:
        for i in range(N_g, N_gs):
            print(input_sents[i], file=f)
    """


def unified_silver_bronze(ext, lang):
    input_file = f"data/{lang}/silver_bronze/train.txt.raw.char.{ext}"
    output_file = f"data/{lang}/silver/train.txt.raw.char.{ext}"
    with open(input_file, "r") as f:
        input_sents = [s.strip() for s in f.readlines()]
    with open(output_file, "r") as f:
        N = len([s.strip() for s in f.readlines()])
    with open(output_file, "w") as f:
        for i in range(N):
            print(input_sents[i], file=f)


def concat_file(ext, lang):
    if lang == "en":
        unified_gold_silver(ext, "en")
    elif lang == "de":
        unified_gold_silver_bronze(ext, "de")
    else:
        unified_silver_bronze(ext, lang)


def generate_normal_char(lang):
    ext = "sent"
    for div, split in DIV_SPLIT_DICT[lang]:
        ngram(lang, div, split)


def generate_distorted_char(lang):
    exts = ["shuffle.intoken", "shuffle.inline", "random", "unify"]
    for div, split in DIV_SPLIT_DICT[lang]:
        shuffle_intoken(lang, div, split)
        shuffle_inline(lang, div, split)
        gen_random(lang, div, split)
        unify(lang, div, split)
    for ext in exts:
        concat_file(ext, lang)


def generate_ngram(lang, n=2):
    ext = f"{n}gram"
    for div, split in DIV_SPLIT_DICT[lang]:
        ngram(lang, div, split, n)


def main(args):
    # normal char file
    for lang in LANGUAGES:
        generate_normal_char(lang)
        generate_distorted_char(lang)
        generate_ngram(lang, args.ngram)


if __name__ == "__main__":
    args = create_arg_parser()
    main(args)
