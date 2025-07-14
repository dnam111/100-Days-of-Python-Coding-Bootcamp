import art
import random

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
    return sum(hand)

print(art.logo)
print("\n" * 3)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

yes_no_play = True

while yes_no_play:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == "y":
        player_cards = []
        computer_cards = []

        player_cards.append(random.choice(cards))
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {player_cards}, current score: {player_score if player_score != 0 else 'Blackjack!'}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0:
            print("You got a Blackjack! You win!")
        elif player_score > 21:
            print("You went over. You lose.")
        else:
            while player_score <= 21:
                another_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if another_card == "y":
                    player_cards.append(random.choice(cards))
                    player_score = calculate_score(player_cards)
                    print(f"Your cards: {player_cards}, current score: {player_score}")
                    if player_score > 21:
                        print("You went over. You lose.")
                        break
                else:
                    while computer_score != 0 and computer_score < 17:
                        new_card = random.choice(cards)
                        computer_cards.append(new_card)
                        computer_score = calculate_score(computer_cards)

                    print(f"Computer's cards: {computer_cards}, final score: {computer_score if computer_score != 0 else 'Blackjack!'}")
                    print(f"Your final hand: {player_cards}, final score: {player_score if player_score != 0 else 'Blackjack!'}")

                    if computer_score == 0:
                        print("Computer got a Blackjack. You lose.")
                    elif player_score > 21:
                        print("You went over. You lose.")
                    elif computer_score > 21:
                        print("Opponent went over. You win.")
                    elif player_score > computer_score:
                        print("You have a larger hand. You win!")
                    elif player_score < computer_score:
                        print("You have a smaller hand. You lose!")
                    else:
                        print("It's a draw!")
                    break

        replay = input("Do you want to play another round? Type 'y' or 'n': ")
        if replay == "n":
            yes_no_play = False
    else:
        yes_no_play = False
