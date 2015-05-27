"""
Objective: Make a hangman game

Specifics:
Player is presented with the number of letters in a mystery word and given a number of attempts they are allowed before they fail

Player guesses a letter, and the game either fills the word in with that letter or reduces the number of attempts they have remaining.
"""
import random
import sys


class RandomWord(object):
    """ Class for getting a random word from the passed-in filename """
    def __init__(self, filename):
        self.filename = filename

        with open(self.filename) as f:
            words_list = []

            for line in f:
                words_list.append(line.rstrip('\r\n'))

            self.word = random.choice(words_list)

    def display_word(self, guessed_letters_list):
        """ Function to display the secret word with the letters that have been correctly guessed. """
        word_to_display = ""

        for letter in self.word:
            if letter in guessed_letters_list:
                word_to_display += " " + letter + " "

            else:
                word_to_display += " _ "

        print "This is your word so far:", word_to_display, "\n"
        return word_to_display


class HangmanPicture(object):

    HANGMAN_PICS = ["", "O", "O-", "O-|", "O-|-", "O-|-<"]

    def __init__(self):
        self.hangman = self.HANGMAN_PICS[0]

    def draw(self, num_incorrect_guesses_made):
        """
        Function to display the updated status of the hangman based on
        the number of incorrect guesses the player has made.
        """
        self.hangman = self.HANGMAN_PICS[num_incorrect_guesses_made]
        print self.hangman

        if num_incorrect_guesses_made == 5:
            print "You died!"

    def __str__(self):
        return self.hangman


class Game(object):
    """ The main game class for creating a new hangman game """

    wrong_answer_putdowns = ["NOPE!",
                             "Wow, you suck at hangman.",
                             "Your guy doesn't stand a chance!",
                             "You're leaving him high and dry"]

    num_incorrect_guesses_made = 0
    guessed_letters = []

    def __init__(self, filename):
        self.secret_word = RandomWord(filename)
        self.hangman = HangmanPicture()

        print type(self.secret_word)

    def play(self):
        """ The main function that begins a new game of hangman. """

        print "\n****** Welcome to Hangman! ******\n"

        option = raw_input("Do you need the rules explained to you? Y/n: ")

        if option.lower() == "y":
            print "\nInstructions:\n" \
                  "A word will be chosen at random from the dictionary. Each turn you guess a letter.\n" \
                  "Every time you guess a letter that isn't in the word, your man gets closer to being hanged!\n" \
                  "When your hangman looks like this: O-|-< ...you're dead!\n" \

        print "Let's play hangman!\n"

        while self.num_incorrect_guesses_made < 5:
            letter_guess = raw_input("Please guess a letter: ").lower()

            # Don't let them guess a non-alpha letter.
            while letter_guess.isalpha() is False:
                letter_guess = raw_input("No special characters allowed! Only enter a letter, please: ").lower()

            # Once a valid letter is chosen, add it to guessed_letters
            if letter_guess not in self.guessed_letters:
                self.guessed_letters.append(letter_guess)

                if letter_guess not in self.secret_word.word:
                    print random.choice(self.wrong_answer_putdowns)
                    self.num_incorrect_guesses_made += 1
                    self.hangman.draw(self.num_incorrect_guesses_made)

                else:
                    print "You chose wisely!\n"
                    self.hangman.draw(self.num_incorrect_guesses_made)

            else:
                print "You've already guessed the letter '%s', please choose a new letter." % letter_guess

            current_word = self.secret_word.display_word(self.guessed_letters)

            print "These are the letters you've already guessed: ", self.guessed_letters

            if "_" not in current_word:
                print "Congratulations! You've won!"
                sys.exit()

game = Game("words.txt")
game.play()
