from random import choice

class Hangman():
    def __init__(self, word_list, num_lives=5):
        self.word = choice(word_list)
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
        
        self.word_guessed = self.current_blanks()
        self.num_letters = self.unique_letters()
        return None
    
    def check_guess(self, guess):
        self.guess = guess
        if self.guess.lower() in self.word:
            print(f"Good guess! {self.guess} is in the word {self.word}.")
            print(self.current_blanks())
            return True
        else:
            self.num_lives -= 1
            print(f"Sorry, {self.guess} is not in the word. Try again.")
            print(f"ou have {self.num_lives} lives left.")
            return False
            
    def ask_for_input(self):
        while True:
            self.guess = input("Guess a letter please: ")
            if len(self.guess) != 1 or not self.guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self.guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                if self.check_guess(self.guess):
                    self.list_of_guesses.append(self.guess)
                    break
                break
                
    def current_blanks(self):
        return [letter if letter in self.list_of_guesses else '_' for letter in self.word]
         
    def unique_letters(self):
        return list(set([letter for letter in self.word if letter not in self.list_of_guesses]))

    
    
word_list = ['orange', 'lychee', 'grapes', 'kiwi', 'banana']
game = Hangman(word_list, 3)
print(game.ask_for_input())

        