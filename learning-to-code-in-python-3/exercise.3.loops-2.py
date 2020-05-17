#!/usr/bin/env python3

import random

take_turn = True
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']

while ( take_turn ):
    random_color = random.choice(colors)
    selected = input(f"Pick a color [{', '.join(colors)}]: ")
    
    print(f"You chose {selected}. The computer chose {random_color}.")
    
    answer = input(f"Would you like to play again? [Y/N]: ").upper()

    if ( answer != 'Y' ):
        take_turn = False