import art
import random
print(art.logo)
print("\n"*2)
# easy attempts = 10 hard attempts = 5
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
random_number = random.randint(1,100)
def guessing_game(attempt):
    while attempt>0:
        print(f"You have {attempt} attempts remaining to guess a number.")
        user_guess = int(input("Make a guess: "))
        if user_guess > random_number:
            print(f"Too high.\nGuess again.")
        elif user_guess < random_number:
            print(f"Too low.\nGuess again.")
        else:
            print(f"You got it! The answer was {random_number}")
            return
        attempt -= 1
    print(f"You've run out of guesses.\nThe answer was {random_number}\nRefresh the page to run again.")

if difficulty == "easy":
    guessing_game(10)
else:
    guessing_game(5)

