import random

# Variable Examples
colors_list = ['R', 'O', 'Y', 'G', 'B', 'W', 'P', 'V']
response_list = ['x', 'y', 'z']
solution_list = ['', '', '', '', '']
round = 0
a = ''
b = ''
c = ''
d = ''
e = ''
player_guess = [a, b, c, d, e]


# Methods
def solution_key_generate():
    return None

def is_right_color():
    return None

def is_right_position():
    return None

def ask_to_play_game():
    start_game = ''
    while start_game != 'Y':
        print("Hello! Welcome to CODEBREAKER!")
        print("Start game? (Y/N)")
        start_game = input()
        if start_game == "N":
            #Exit game
            pass
    



# Game start
print("Hello! Welcome to CODEBREAKER!")
print("Start game? (Y/N)")
start_game = input()

    
while round < 12:
    print("Please Guess the code by choosing 5 colors, 1 of each, from the following 8 choices")
    print("'R', 'O', 'Y', 'G', 'B', 'W', 'P', 'V'")
    guess = input()
    if len(guess) < 5:
        #repeat prompt
        pass
    
    
    
    
    round += 1