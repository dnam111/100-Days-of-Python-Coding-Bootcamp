import art
import game_data
import random
print(art.logo)
guess_correct = True
score = 0
while guess_correct:
    first_choice = random.choice(game_data.data)
    second_choice = random.choice(game_data.data)
    while second_choice == first_choice:
        second_choice = random.choice(game_data.data)
    print(f"Compare A: {first_choice['name']}, {first_choice['description']}, from {first_choice['country']} ")
    print(art.vs)
    print(f"Against B: {second_choice['name']}, {second_choice['description']}, from {second_choice['country']} ")
    question = input("Who has more followers? Type 'A' or 'B': ").lower()
    first_followers = first_choice['follower_count']
    second_followers = second_choice['follower_count']
    if (question == 'a' and first_followers > second_followers) or (question == 'b' and second_followers > first_followers):
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        guess_correct = False
        print(f"Sorry, that's wrong. Final score {score}.")



