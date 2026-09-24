import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
dealer_cards = []


def add_to_list(list_name):
    random_choice = random.choice(cards)
    list_name.append(random_choice)
    return random_choice


consent = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
print("\n" * 100)
print(art.logo)

add_to_list(your_cards)
add_to_list(your_cards)
add_to_list(dealer_cards)
add_to_list(dealer_cards)

is_game_over = False

while not is_game_over:
    your_score = sum(your_cards)
    dealer_score = sum(dealer_cards)

    # Auto-adjust Ace if busted at start or after a draw
    if your_score > 21 and 11 in your_cards:
        your_cards[your_cards.index(11)] = 1
        your_score = sum(your_cards)

    print(f"Your cards: {your_cards}, current score: {your_score}\nComputer's first card: {dealer_cards[0]}")

    if your_score > 21:
        print("You went over 21. You lose!")
        is_game_over = True
    else:
        want_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if want_card == "y":
            add_to_list(your_cards)
        else:
            # Dealer draws continuously until score is at least 17
            while dealer_score < 17:
                add_to_list(dealer_cards)
                dealer_score = sum(dealer_cards)

            print(
                f"Your final hand: {your_cards}, final score: {your_score}\nComputer's final hand: {dealer_cards}, final score: {dealer_score}")

            if dealer_score > 21:
                print("Opponent went over. You win!")
            elif dealer_score > your_score:
                print("You lose!")
            elif dealer_score == your_score:
                print("Draw!")
            elif your_score > dealer_score:
                print("You win!")

            is_game_over = True