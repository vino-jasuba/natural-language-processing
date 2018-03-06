from nltk.corpus import inaugural
from nltk.corpus import reuters
from nltk.corpus import brown
from nltk.corpus import nps_chat
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import random
import numpy as np


def zipf_plot(string_list):
    #   first let's change everything to lowercase
    words = [w.lower() for w in string_list]
    dist = FreqDist(words)
    #   make sure the result is sorted (taking advantage of most_common because it sorts in decreasing frequency)
    dist = dist.most_common()
    #   we plot
    values = [k[1] for k in dist]

    rank = np.arange(1, len(values) + 1)
    ax = plt.subplot()
    plt.yscale('log')
    plt.xscale('log')

    #   make the rank such that the higher value has lower rank
    plt.xlabel('frequency rank')
    plt.ylabel('absolute frequency')
    ax.plot(rank, values, 'b-o')
    plt.show()

    #   return in sorted order
    return dist


def generate_text(word_count=100, characters='abcdefg '):
    string = ''
    l = 0

    while l <= word_count:
        choice = random.choice(characters)
        if choice == ' ':
            l += 1
        string += choice
    # return randomly generated string
    return string


text = generate_text(50000)

zipf_plot(text.split())

# zipf_plot(reuters.words())

