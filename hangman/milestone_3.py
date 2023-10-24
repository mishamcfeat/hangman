# Task 1:
# while True:
#     guess = input("Guess a letter please: ")
#     if guess.isalpha():
#         break
#     else:
#         print("Invalid letter. Please, enter a single alphabetical character.")     

# Task 2:       
# while True:
#     word = 'apple'
#     guess = input("Guess a letter please: ").lower()
    
#     if len(guess) == 1 and guess.isalpha():
#         if guess in word:
#             print(f"Good guess! {guess} is in the word {word}.")
#             break
#         else:
#             print(f"Sorry, {guess} is not in the word. Try again.")
#     else:
#         print("Please enter a single alphabetical character.")   
        
# Task 3:
def check_guess(guess):
    word = 'apple'
    if guess.lower() in word:
        return f"Good guess! {guess} is in the word {word}."
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
            
def ask_for_input():
    while True:
        guess = input("Guess a letter please: ")
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
   
ask_for_input()