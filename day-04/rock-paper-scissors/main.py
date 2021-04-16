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
def play_round():
    rps = [rock, paper, scissors]
    cpu_pick = random.choice(rps)
    player_pick = input("Rock, paper, or scissors?")
    if player_pick == "rock":
        if cpu_pick == scissors:
            print(f"You picked {rock}")
            print(f"CPU picked {scissors}")
            print("You win!")
        elif cpu_pick == paper:
            print(f"You picked {rock}")
            print(f"CPU picked {paper}")
            print("You lose!")
        else:
            print(f"You picked {rock}")
            print(f"CPU picked {rock}")
            print("Draw! Play again!")
            play_round()
    if player_pick == "paper":
        if cpu_pick == rock:
            print(f"You picked {paper}")
            print(f"CPU picked {rock}")
            print("You win!")
        elif cpu_pick == scissors:
            print(f"You picked {paper}")
            print(f"CPU picked {scissors}")
            print("You lose!")
        else:
            print(f"You picked {paper}")
            print(f"CPU picked {paper}")
            print("Draw! Play again!")
            play_round()
    if player_pick == "scissors":
        if cpu_pick == paper:
            print(f"You picked {scissors}")
            print(f"CPU picked {paper}")
            print("You win!")
        elif cpu_pick == rock:
            print(f"You picked {scissors}")
            print(f"CPU picked {rock}")
            print("You lose!")
        else:
            print(f"You picked {scissors}")
            print(f"CPU picked {scissors}")
            print("Draw! Play again!")
            play_round()
play_round()
