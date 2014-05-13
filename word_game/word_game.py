# Exercise one:

# Given a file containing all words in the Oxford dictionary, delimited by a
# newline, create a program which reads a word from a user and finds all words
# which may be constructed from the letters in that word.
from itertools import permutations


def get_word_set(length=None):
    with open('words.txt') as f:
        word_set = set()

        for word in f:
            word = word.rstrip()

            if length is None:
                word_set.add(word)
            elif len(word) == length:
                word_set.add(word)

    return word_set


def find_words(val, n=None):
    word_set = get_word_set()

    continue_looping = True

    if n is None:
        n_supplied = False
        n = len(val)
    else:
        n_supplied = True

    results = set()

    while n > 0 and continue_looping is True:
        perms = permutations(val, n)
        for perm in perms:
            string_perm = ''.join(perm)
            if string_perm in word_set:
                results.add(string_perm)

        n -= 1

        if n_supplied is True:
            continue_looping = False

    return results

    # for w in sorted(results):
    #     print w

# val = raw_input('Enter a word: ')
# find_words(val)

# Exercise two:

# Given a file containing all words in the Oxford dictionary, delimited by a
# newline, prompt the users with a scrambled word and ask them to find all
# other words that can be formed from the letters provided. Show the user how
# many words of a given length remain.


def shuffle_word(word):
    from random import shuffle

    word = list(word)
    shuffle(word)
    return ''.join(word)


def scrambled_words():
    word_list = list(get_word_set(6))

    from random import choice
    selected_word = choice(word_list)

    # print selected_word + ': '
    print shuffle_word(selected_word) + ': '

    len6 = list(find_words(selected_word, 6))
    len5 = list(find_words(selected_word, 5))
    len4 = list(find_words(selected_word, 4))

    len6_found = []
    len5_found = []
    len4_found = []

    print "\nFound four letter words: " + str(len6_found)
    print str(len(len6) - len(len6_found)) + " six letter words left."
    print "Found five letter words: " + str(len5_found)
    print str(len(len5) - len(len5_found)) + " five letter words left."
    print "Found six letter words: " + str(len4_found)
    print str(len(len4) - len(len4_found)) + " four letter words left."

    user_choice = raw_input("\nEnter a word: ")



scrambled_words()