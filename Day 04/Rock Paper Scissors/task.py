import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]
user_input = int(input("What do you chose? Type 0 for Rock, 1 for Paper, 2 for Scissors:\n "))
if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input == 2:
    print(scissors)
else:
    print("Invalid input")
print("Computer chose:")
computer_move = moves[random.randint(0,2)]
print(computer_move)
if user_input == 0 and computer_move == paper:
    print("You lose!")
elif user_input == 0 and computer_move == scissors:
    print("You win!")
elif user_input == 0 and computer_move == rock:
    print("It's a draw!")
elif user_input == 1 and computer_move == paper:
    print("It's a draw")
elif user_input == 1 and computer_move == scissors:
    print("You lose!")
elif user_input == 1 and computer_move == rock:
    print("You win!")
elif user_input == 2 and computer_move == rock:
    print("You lose!")
elif user_input == 2 and computer_move == paper:
    print("You win!")
elif user_input == 2 and computer_move == scissors:
    print("It's a draw")

