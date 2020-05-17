#!/usr/bin/env python3

data_valid = False

things = 20

try:
    people = int( input("How many people are getting things?: ") )
    things_per_person = things / people

    print(f"Each person gets {things_per_person} thing(s)")
except BaseException as e: 
    print(f"Something bad happend: {e}")