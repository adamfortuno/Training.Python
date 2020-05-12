#!/usr/bin/env python3

import random

names = []

while ( len(names) < 8 ):
    name = input("Give me another name, please: ")
    names.append(name)

print(f"You chose {random.choice(names)}")