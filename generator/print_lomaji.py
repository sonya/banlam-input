#!/usr/bin/env python3

from phonemes import generate_all_sequences

combos = generate_all_sequences()

for input_sequence in sorted(combos.keys()):
    output_sequence = combos[input_sequence]
    print('{} {}'.format(input_sequence, output_sequence))
