#1 pick 2 randoms which aren't same.
#2 Make b to a
#3 count score and display at end.

import art
import game_data
import random
score = 0
game_over = False
print(art.logo)
def comparison():
    item_a = random.choice(game_data.data)
    item_b = random.choice(game_data.data)
    while item_a == item_b:
        item_b = random.choice(game_data.data)
    return item_a, item_b
item_a, item_b = comparison()

def user_choice():
    print(f"Compare A: {item_a["name"]}, a {item_a["description"]}, from {item_a['country']}")
    print(art.vs)
    print(f"Compare B: {item_b["name"]}, a {item_b["description"]}, from {item_b['country']}")
    choice = input("Who has more followers? Type 'A' or 'B': ")
    return choice


while game_over == False:
    Choice = user_choice().lower()
    while Choice != "a" and Choice != "b":
        Choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if Choice == "a" and item_a["follower_count"] > item_b["follower_count"]:
        score += 1
        print(f"You're right! Current score is {score}")
        item_a = item_b
        item_b = random.choice(game_data.data)
        while item_a == item_b:
            item_b = random.choice(game_data.data)
    elif Choice == "b" and item_b["follower_count"] > item_a["follower_count"]:
        score += 1
        print(f"You're right! Current score is {score}")
        item_a = item_b
        item_b = random.choice(game_data.data)
        while item_a == item_b:
            item_b = random.choice(game_data.data)
    else:
        print(f"Sorry, That's wrong. Final score is {score}")
        game_over = True
