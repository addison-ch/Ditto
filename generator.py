from collections import defaultdict
import random


def fix_word(word):
    n = ""
    for l in range(len(word)):
        if str(l).isalnum() or l == '!' or l == "." or l == '?' or l == "," or l == "'":
            n += word[l]
    return(n)


def create_markov_chain(text):
    words = text.split()
    markov_dict = defaultdict(list)

    for current_word, next_word in zip(words[0:-1], words[1:]):
        current_word = fix_word(current_word)
        next_word = fix_word(next_word)
        markov_dict[current_word].append(next_word)

    markov_dict = dict(markov_dict)
    return markov_dict


def update_chain(data, chain, query):

    for item in data:
        a = create_markov_chain(item[query])

        for x, y in a.items():
            if x in chain.keys():
                chain[x] += y
            else:
                chain[x] = y

    return chain


def gen_sentence(chain, words):

    correct_start = False

    while correct_start == False:
        word1 = random.choice(list(chain.keys()))
        if word1[0].isupper():
            correct_start = True

    word2 = ""

    sentence = word1

    count = 1

    while count < words:
        count += 1

        word2 = random.choice(chain[word1])

        if not word2 in chain.keys():
            count = words

        sentence += " " + word2

        word1 = word2

    return sentence
