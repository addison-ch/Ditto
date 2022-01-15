import json
import re

vowels = "aeiou"


def count_syllables_self(word):  # https://eayd.in/?p=232
    word = word.lower()
    syllable_count = 0
    syllables_removed = 0

    if word[-2:] == "es" or word[-2:] == "ed":
        double_and_triple_1 = len(re.findall(r"[eaoui][eaoui]", word))
        if double_and_triple_1 > 1 or len(re.findall(r"[eaoui][^eaoui]", word)) > 1:
            if (
                word[-3:] == "ted"
                or word[-3:] == "tes"
                or word[-3:] == "ses"
                or word[-3:] == "ied"
                or word[-3:] == "ies"
            ):
                pass
            else:
                syllables_removed += 1
    if word[-2:] == "ie":
        if word[-3:][0] in vowels:
            pass
        else:
            syllable_count += 1
    if word[-1:] == "e":
        if word[-2:] == "le":
            pass
        else:
            syllables_removed += 1

    double_and_triple = len(re.findall(r"[eaoui][eaoui]", word))
    triple = len(re.findall(r"[eaoui][eaoui][eaoui]", word))
    syllables_removed += double_and_triple + triple

    num_vowels = len(re.findall(r"[eaoui]", word))

    if word[:2] == "mc":
        syllable_count += 1
    if word[-1:] == "y" and word[-2] not in vowels:
        syllable_count += 1
    for i, j in enumerate(word):
        if j == "y":
            if (i != 0) and (i != len(word) - 1):
                if word[i - 1] not in vowels and word[i + 1] not in vowels:
                    syllable_count += 1
    if word[:3] == "tri" and word[3] in vowels:
        syllable_count += 1
    if word[:2] == "bi" and word[2] in vowels:
        syllable_count += 1
    if word[-3:] == "ian":
        if word[-4:] == "cian" or word[-4:] == "tian":
            pass
        else:
            syllable_count += 1
    if word[:2] == "co" and word[2] in vowels:
        syllable_count += 1
    if word[:3] == "pre" and word[3] in vowels:
        syllable_count += 1

    final_count = num_vowels - syllables_removed + syllable_count
    if final_count != 0:
        return final_count
    else:
        return len(word)


def count_syllables_from_data(word):
    file = open("syllable_counting/syllables.json")
    syllables_list = json.load(file)

    try:
        word_uppercase = word.upper()
        return syllables_list[word_uppercase]
    except KeyError:
        file2 = open("syllable_counting/commonacronyms.json")
        acronyms_list = json.load(file2)
        if word.upper() in acronyms_list.values():
            return len(word)
        else:
            return count_syllables_self(word)
