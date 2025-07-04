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
play= [rock, paper, scissors]
computerrandom=random.randint(0,2)
playerchoice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors: "))
print(f"{play[playerchoice]}")
print(f"Computer chose {play[computerrandom]}")
if playerchoice == 0 and computerrandom == 2:
    print("You win!")
elif playerchoice == 0 and computerrandom == 1:
    print("You lose")
elif playerchoice == 1 and computerrandom == 0:
    print("You win!")
elif playerchoice == 1 and computerrandom == 2:
    print("You lose")
elif playerchoice == 2 and computerrandom == 1:
    print("You win!")
elif playerchoice == 2 and computerrandom == 0:
    print("You lose")
elif computerrandom == playerchoice:
    print("Draw")

