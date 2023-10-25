from random import choice

class Hangman:
    
    def __init__(self, word_list, num_lives=5):
        self.word = choice(word_list)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
    
    def check_guess(self, guess):
        if guess.lower() in self.word:
            print(f"Good guess! {guess} is in the word {self.word}.")
            return True
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")
            return False
            
    def ask_for_input(self):
        while True:
            guess = input("Guess a letter please: ")
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                if self.check_guess(guess):
                    self.list_of_guesses.append(guess)
                    self.word_guessed = [letter if letter in self.list_of_guesses else '_' for letter in self.word]
                else:
                    self.list_of_guesses.append(guess)  # We should also add incorrect guesses to the list
                break

    
    
word_list = ['orange', 'lychee', 'grapes', 'kiwi', 'banana']
game = Hangman(word_list, 3)
print(game.ask_for_input())

        