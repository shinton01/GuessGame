print('Guessing game')
print('------------------------')
print('Can you guess the number?')
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

# Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
# 1. What do I want to repeat?
#  ->
# 2. What do I want to change each time?
#  ->
# 3. How long should we repeat?
#  ->

number_to_guess = 64
guess_count = 1
guess_limit = 5
guess = int(input('Try to guess the number 1-100 '))
while guess_count < guess_limit:
    if guess != number_to_guess:
        guess_count += 1
        if guess < number_to_guess:
            guess = int(input('Sorry. Your number is too low. Try again '))
        else:
            guess = int(input('Sorry. Your number is too high. Try again '))
    if guess == number_to_guess:
        print(f'Yeah!!! The number is {number_to_guess}')
        break

if guess != number_to_guess:
    print(f'Sorry you lose! It was {number_to_guess}')
