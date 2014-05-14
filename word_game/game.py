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


def permutation_game():
    val = raw_input('Enter a word: ')
    results = find_words(val)
    for w in sorted(results):
        if len(w) > 3:
            print w
    print

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
    shuffled_word = shuffle_word(selected_word) + ': '

    len6 = list(find_words(selected_word, 6))
    len5 = list(find_words(selected_word, 5))
    len4 = list(find_words(selected_word, 4))

    len6_found = []
    len5_found = []
    len4_found = []

    print "Enter 's' to save and quit to the menu."
    print "Enter 'q' to quit to the menu without saving."

    while len6 or len5 or len4:
        print
        print shuffled_word

        print "\nFound four letter words: " + str(len6_found)
        print str(len(len6)) + " six letter words left."
        print "Found five letter words: " + str(len5_found)
        print str(len(len5)) + " five letter words left."
        print "Found six letter words: " + str(len4_found)
        print str(len(len4)) + " four letter words left."

        user_choice = raw_input("\nEnter a word: ")

        if user_choice == 'q':
            print
            return
        if user_choice == 's':
            save_game_name = raw_input("\nEnter a name for the saved game: ")
            with open('savedgames.txt', 'w') as f:
                f.write(save_game_name + '\n')
                f.write(shuffled_word + '\n')
                f.write(str(len4) + '\n')
                f.write(str(len5) + '\n')
                f.write(str(len6) + '\n')
                f.write(str(len4_found) + '\n')
                f.write(str(len5_found) + '\n')
                f.write(str(len6_found) + '\n')
                f.write('\n')

            print
            return


        if user_choice in len6 or user_choice in len5 or user_choice in len4:
            print "Found word!"

            if user_choice in len6:
                len6_found.append(user_choice)
                len6.remove(user_choice)
            elif user_choice in len5:
                len5_found.append(user_choice)
                len5.remove(user_choice)
            elif user_choice in len4:
                len4_found.append(user_choice)
                len4.remove(user_choice)
        else:
            print "Not a valid choice."

    print "You won the game!"


def main():
    while True:
        print "Enter a number to play a game."
        print "1: word guessing game."
        print "2: word guessing game solver."
        user_choice = raw_input("> ")

        if user_choice == '1':
            scrambled_words()
        elif user_choice == '2':
            permutation_game()
        else:
            print "Not a valid choice. Please enter a valid choice."
main()


