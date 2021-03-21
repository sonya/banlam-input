#!/usr/bin/env python3

import csv
import os
import re

from phonemes import generate_all_sequences

src_dir = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    '..',
    'moedict-data-twblg',
    'uni')

word_filename = '詞目總檔.csv'

word_path = os.path.join(src_dir, word_filename)

lomaji_sequences = generate_all_sequences()
lomaji_sequences = {v: k for k, v in lomaji_sequences.items()}

hanji_combos = {}

def add_sequence(input_sequence, output_sequence):
    if input_sequence not in hanji_combos:
        hanji_combos[input_sequence] = set()
    hanji_combos[input_sequence].add(output_sequence)


def sanitize_word(word_compound):
    # remove 輕聲 (ignoring for now)
    # clean up hyphen lookalikes
    # remove punctuation
    return word_compound.lower().strip()\
        .replace('--', '-')\
        .replace('‑', '-')\
        .replace(',', '')\
        .replace('.', '')\
        .replace('?', '')\
        .replace(';', '')


with open(word_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        tailo = row['音讀']
        hanji = row['詞目'].strip()

        versions = tailo.split('/')
        for version in versions:
            word_compound = sanitize_word(version)
            tokens = re.split('[ \-]', word_compound)
            if len(tokens) == 1:
                if word_compound == '':
                    continue # there are many actual empty entries

                if word_compound not in lomaji_sequences:
                    continue # at some point we can generate a list to debug

                input_sequence = lomaji_sequences[word_compound]
                add_sequence(input_sequence, hanji)
            else:
                compound_input_tokens = []
                for token in tokens:
                    if token == '':
                        continue # happens for leading 輕聲

                    if token not in lomaji_sequences:
                        continue

                    regular_sequence = lomaji_sequences[token]
                    simplified_sequence = re.sub('\d', '', regular_sequence)
                    compound_input_tokens.append(simplified_sequence)
                input_sequence = '-'.join(compound_input_tokens)
                add_sequence(input_sequence, hanji)

for input_sequence in sorted(hanji_combos.keys()):
    output_sequence_set = hanji_combos[input_sequence]
    output_sequence = ','.join(list(output_sequence_set))
    print('{} {}'.format(input_sequence, output_sequence))
