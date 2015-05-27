"""
Objective: Take the hangman game and make it object-oriented.

Classes: Word, Hangman, Game
"""

import random
import sys


class RandomWord(object):
    """
    read the words from an outside file and return one of those words, randomly chosen
    """

    def __init__(self, filename):

        with open(filename) as f:
            words_list = []

            for line in f:
                words_list.append(line.rstrip('\r\n'))

            self.word = random.choice(words_list)

    def display(self, guessed_letters_list):
        """
        Function to display the secret word with the letters that have been correctly guessed.
        """
        word_to_display = ""

        for letter in self.word:
            if letter in guessed_letters_list:
                word_to_display += " " + letter + " "

            else:
                word_to_display += " _ "

        print "This is your word so far:", word_to_display, "\n"
        return word_to_display


class Hangman(object):

    HANGMAN_PICS = ["", "O", "O-", "O-|", "O-|-", "O-|-<"]

    def __init__(self):
        self.hangman = self.HANGMAN_PICS[0]

    def draw(self, num_incorrect_guesses_made):
        """
        Function to display the updated status of the hangman based on the number of incorrect guesses the player has made.
        """

        self.hangman = self.HANGMAN_PICS[num_incorrect_guesses_made]
        print self.hangman

        if num_incorrect_guesses_made == 5:
            print "You died!!"


class Game(object):

    WRONG_ANSWER_PUTDOWNS = ["NOPE!",
                             "Wow, you suck at hangman.",
                             "Your guy doesn't stand a chance!",
                             "You're leaving him high and dry"]

    def __init__(self, filename):
        self.secret_word = RandomWord(filename)
        self.hangman = Hangman()
        self.num_incorrect_guesses_made = 0
        self.guessed_letters = []

    def play(self):
        """
        The main function that begins a new game of hangman.
        """

        print "\n****** Welcome to Hangman! ******\n"

        option = raw_input("Do you need the rules explained to you? Y/n: ")

        if option.lower() == "y":
            print "\nInstructions:\n" \
                  "A word will be chosen at random from the dictionary. Each turn you guess a letter.\n" \
                  "Every time you guess a letter that isn't in the word, your man gets closer to being hanged!\n" \
                  "When your hangman looks like this: O-|-< ...you're dead!\n" \

        print "Let's play hangman!\n"

        # Initialize the number of incorrect guesses made to 0
        while self.num_incorrect_guesses_made < 5:
            if len(self.guessed_letters) == 0:
                self.secret_word.display(self.guessed_letters)

            letter_guess = raw_input("Please guess a letter: ").lower()

            # Don't let them guess a non-alpha letter.
            while letter_guess.isalpha() is False:
                letter_guess = raw_input("No special characters allowed! Only enter a letter, please: ").lower()

            # Once a valid letter is chosen, add it to guessed_letters
            if letter_guess not in self.guessed_letters:
                self.guessed_letters.append(letter_guess)

                if letter_guess not in self.secret_word.word:
                    print random.choice(self.WRONG_ANSWER_PUTDOWNS)
                    self.num_incorrect_guesses_made += 1
                    self.hangman.draw(self.num_incorrect_guesses_made)

                else:
                    print "You chose wisely!\n"
                    self.hangman.draw(self.num_incorrect_guesses_made)

            else:
                print "You've already guessed the letter '%s', please choose a new letter." % letter_guess

            current_word = self.secret_word.display(self.guessed_letters)

            print "These are the letters you've already guessed: ", self.guessed_letters

            if "_" not in current_word:
                print "Congratulations! You've won!"
                sys.exit()

game = Game("../word_game/words.txt")
game.play()
