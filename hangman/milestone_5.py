from random import choice

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game.
    num_lives: int
        Number of lives the player has.

    Attributes:
    ----------
    word: str
        The word to be guessed, picked randomly from the word_list.
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed.
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet.
    num_lives: int
        The number of lives the player has.
    list_of_guesses: list
        A list of the letters that have already been tried.

    Methods:
    -------
    _check_guess(guess)
        Checks if the letter is in the word and updates the game state.
        Underscore is to indicate that it is a protected class.
    _ask_for_input()
        Asks the user for a letter and validates the input.
        Underscore is to indicate that it is a protected class.
    '''

    def __init__(self, word_list, num_lives=5):
        '''
        Initialises the Hangman game.

        Parameters:
        ----------
        word_list: list
            List of words to be used in the game.
        num_lives: int, optional
            Number of lives the player starts with. Default is 5.
        '''
        self.word = choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

        print(f"The mistery word has {self.num_letters} characters")
        print(' '.join(self.word_guessed))

    def _check_guess(self, guess):
        '''
        Checks if the given letter is in the word and updates game state accordingly.

        Parameters:
        ----------
        guess: str
            The letter that the player guessed.
        '''
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[idx] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

        # Display the current state of the guessed word after each guess
        print(' '.join(self.word_guessed))

    def _ask_for_input(self):
        '''
        Asks the user for a letter guess and handles input validation.
        '''
        while True:
            guess = input("Guess a letter: ")
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self._check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    '''
    Starts and manages the Hangman game until it ends.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game.
    '''
    game = Hangman(word_list, num_lives=5)
    while game.num_lives > 0 and game.num_letters > 0:
        game._ask_for_input()
    if game.num_letters == 0:
        print("Congratulations! You won!")
    else:
        print(f"You lost! The word was {game.word}")

if __name__ == '__main__':
    word_list = ['orange', 'lychee', 'grapes', 'kiwi', 'banana']
    play_game(word_list)
