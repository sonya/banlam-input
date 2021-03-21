vowels = {
  'a': {1: 'a', 2: 'á', 3: 'à', 4: 'a', 5: 'â', 6: 'ǎ', 7: 'ā', 8: 'a̍', 9: 'a̋'},
  'e': {1: 'e', 2: 'é', 3: 'è', 4: 'e', 5: 'ê', 6: 'ě', 7: 'ē', 8: 'e̍', 9: 'e̋'},
  'i': {1: 'i', 2: 'í', 3: 'ì', 4: 'i', 5: 'î', 6: 'ǐ', 7: 'ī', 8: 'i̍', 9: 'i̋'},
  'o': {1: 'o', 2: 'ó', 3: 'ò', 4: 'o', 5: 'ô', 6: 'ǒ', 7: 'ō', 8: 'o̍', 9: 'ő'},
  'u': {1: 'u', 2: 'ú', 3: 'ù', 4: 'u', 5: 'û', 6: 'ǔ', 7: 'ū', 8: 'u̍', 9: 'ű'},
  'm': {1: 'm', 2: 'ḿ', 3: 'm̀', 4: 'm', 5: 'm̂', 6: 'm̌', 7: 'm̄', 8: 'm̍', 9: 'm̋'},
  'n': {1: 'n', 2: 'ń', 3: 'ǹ', 4: 'n', 5: 'n̂', 6: 'ň', 7: 'n̄', 8: 'n̍', 9: 'n̋'},
}

start_consts = [
    'p', 'ph', 'm', 'b',
    't', 'th', 'ts', 'tsh', 's', 'n', 'j', 'l',
    'k', 'kh', 'ng', 'g',
    '', 'h']

long_endings = {
    'a': [
        'a', 'ann', 'am', 'an', 'ang',
        'ia', 'iann', 'iam', 'ian', 'iang',
        'ua', 'uann', 'uan', 'uang',
        'ai', 'ainn', 'uai', 'uainn',
        'au', 'iau', 'iaunn',
    ],
    'e': ['e', 'enn', 'ue'],
    'i': ['i', 'inn', 'im', 'in', 'ing', 'ui', 'uinn'],
    'o': ['o', 'oo', 'onn', 'om', 'ong', 'io', 'iong'],
    'u': ['u', 'un', 'iu', 'iunn'],
    'm': ['m'],
    'n': ['ng'],
}

short_endings = {
    'a': [
        'ap', 'at', 'ak', 'ah', 'annh',
        'iap', 'iat', 'iak', 'iah', 'iannh',
        'aih', 'ainnh', 'auh', 'iauh', 'aunnh',
        'uat', 'uah',
    ],
    'e': ['eh', 'ennh', 'ueh'],
    'i': ['ip', 'it', 'ik', 'ih', 'innh', 'uih'],
    'o': ['oh', 'op', 'ok', 'ooh', 'onnh', 'ioh', 'iok'],
    'u': ['ut', 'uh', 'iuh', 'iunnh'],
    'm': ['mh'],
    'n': ['ngh'],
}


def generate_combo(start_const, ending, vowel, tone):
    decorated_vowel = vowels[vowel][tone]
    if vowel == decorated_vowel:
        decorated_ending = ending
        input_sequence = '{}{}'.format(start_const, ending)
    else:
        decorated_ending = ending.replace(vowel, decorated_vowel, 1)
        input_sequence = '{}{}{}'.format(start_const, ending, tone)
    output_sequence = '{}{}'.format(start_const, decorated_ending)
    return (input_sequence, output_sequence)


def generate_tone_groups(start_const, tone, ending_group):
    result = {}

    for (vowel, endings) in ending_group.items():
        for ending in endings:
            (
                input_sequence,
                output_sequence,
            ) = generate_combo(start_const, ending, vowel, tone)

            result[input_sequence] = output_sequence

    return result


def generate_all_sequences():
    result = {}

    for start_const in start_consts:
        for tone in [1, 2, 3, 5, 6, 7, 9]:
            result.update(generate_tone_groups(start_const, tone, long_endings))
        for tone in [4, 8]:
            result.update(generate_tone_groups(start_const, tone, short_endings))

    return result
