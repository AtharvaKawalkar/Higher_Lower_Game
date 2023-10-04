#Higher Lower Game
import Higher_Lower_G_art
from Higher_Lower_G_data import data
import random
import os

clear = lambda: os.system('cls')

def select_A(data):
    A = random.randint(0,len(data)-1)
    return A

def select_B(data):
    B = random.randint(0,len(data)-1)
    return B

print(Higher_Lower_G_art.logo)

status = 'win'
run = 1
last_B = ""
current_score = 0

A = select_A(data)

while(status == 'win'):
    while(run != 1):
        clear()
        print(Higher_Lower_G_art.logo)
        print(f"You're Correct. Your Current score is {current_score}")
        break
    
    print(f"Compare A : {data[A]['name']}, {data[A]['description']}, from {data[A]['country']}")
    print(Higher_Lower_G_art.vs)
    B = select_B(data)
    if(A == B):
        if(last_B == B):
            B = select_B(data)
        B = select_B(data)
    print(f"Compare B : {data[B]['name']}, {data[B]['description']}, from {data[B]['country']}")
    player_choice = input("Who has more followers? Type 'A' or 'B' : ").lower()
    if(player_choice == 'a'):
        player = data[A]['followers']
        non_player = data[B]['followers']
    else:
        player = data[B]['followers']
        non_player = data[A]['followers']
    if(player>non_player):
        status = 'win'
        run = 2
        current_score += 1
        if(player_choice == 'a'):
            A = A
            last_B = B
        else:
            A = B
            last_B = A
    else:
        print("You Lose")
        status = "lose"
else:
    print(f"Your final score is {current_score}")