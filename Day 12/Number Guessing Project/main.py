import random
game_over = False
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = (input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

main_num = random.randint(1, 100)

def guess_number(number):
    global attempts
    global game_over
    if number == main_num:
        print(f"You got it! The answer was {main_num}.")
        game_over = True
    elif  number > main_num:
        print("Too high.")
        attempts -= 1
    elif number < main_num:
        print("Too low.")
        attempts -= 1

    if attempts > 0 and not game_over:
        print("Guess again.")

while not game_over:
    if attempts!=0:
        print(f"You have {attempts} attempts left.")
        guess = int(input("Make a guess: "))
        guess_number(guess)
    elif attempts==0:
        print("You lose.")
        game_over = True