import random

word_list = ['orange', 'lychee', 'grapes', 'kiwi', 'banana']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("Please guess a single letter: ")
if len(guess) == 1 and guess.isalpha():
    print("good guess!")
else:
    print("Oops! That is not a valid input.")

