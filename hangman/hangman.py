"""
Objective: Make a hangman game

Specifics:
Player is presented with the number of letters in a mystery word and given a number of attempts they are allowed before they fail

Player guesses a letter, and the game either fills the word in with that letter or reduces the number of attempts they have remaining.
"""
import random
import sys


def random_word(filename):
    """
    read the words from an outside file and return one of those words, randomly chosen
    """
    with open(filename) as f:
        words_list = []

        for line in f:
            words_list.append(line.rstrip('\r\n'))

        chosen_word = random.choice(words_list)
    return chosen_word


def draw_hangman(num_incorrect_guesses_made):
    """
    Function to display the updated status of the hangman based on the number of incorrect guesses the player has made.
    """

    if num_incorrect_guesses_made == 1:
        hangman = "O"
        print hangman

    elif num_incorrect_guesses_made == 2:
        hangman = "O-"
        print hangman

    elif num_incorrect_guesses_made == 3:
        hangman = "O-|"
        print hangman

    elif num_incorrect_guesses_made == 4:
        hangman = "O-|-"
        print hangman

    elif num_incorrect_guesses_made == 5:
        hangman = "O-|-<"
        print hangman
        print "You died!"


def display_word(secret_word, guessed_letters_list):
    """
    Function to display the secret word with the letters that have been correctly guessed.
    """
    word_to_display = ""

    for letter in secret_word:
        if letter in guessed_letters_list:
            word_to_display += " " + letter + " "

        else:
            word_to_display += " _ "

    print "This is your word so far:", word_to_display, "\n"
    return word_to_display


def play_hangman():
    """
    The main function that begins a new game of hangman.
    """

    intro = "\n****** Welcome to Hangman! ******\n"

    print intro

    option = raw_input("Do you need the rules explained to you? Y/n: ")

    if option.lower() == "y":
        print "\nInstructions:\n" \
              "A word will be chosen at random from the dictionary. Each turn you guess a letter.\n" \
              "Every time you guess a letter that isn't in the word, your man gets closer to being hanged!\n" \
              "When your hangman looks like this: O-|-< ...you're dead!\n" \

    print "Let's play hangman!\n"

    # Get the word from random_word()
    secret_word = random_word("words.txt")

    # Initialize the number of incorrect guesses made to 0
    num_incorrect_guesses_made = 0
    guessed_letters = []

    wrong_answer_putdowns = ["NOPE!",
                             "Wow, you suck at hangman.",
                             "Your guy doesn't stand a chance!",
                             "You're leaving him high and dry"]

    while num_incorrect_guesses_made < 5:
        letter_guess = raw_input("Please guess a letter: ").lower()

        # Don't let them guess a non-alpha letter.
        while letter_guess.isalpha() is False:
            letter_guess = raw_input("No special characters allowed! Only enter a letter, please: ").lower()

        # Once a valid letter is chosen, add it to guessed_letters
        if letter_guess not in guessed_letters:
            guessed_letters.append(letter_guess)

            if letter_guess not in secret_word:
                print random.choice(wrong_answer_putdowns)
                num_incorrect_guesses_made += 1
                draw_hangman(num_incorrect_guesses_made)

            else:
                print "You chose wisely!\n"
                draw_hangman(num_incorrect_guesses_made)

        else:
            print "You've already guessed the letter '%s', please choose a new letter." % letter_guess

        current_word = display_word(secret_word, guessed_letters)

        print "These are the letters you've already guessed: ", guessed_letters

        if "_" not in current_word:
            print "Congratulations! You've won!"
            sys.exit()

play_hangman()
