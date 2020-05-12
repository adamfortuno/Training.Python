#!/usr/bin/env python3

person = {
    "name": "Peter Parker",
    "gneder": "Male",
    "age": "38",
    "address": "12 Barnard Street, West Chester, PA",
    "phone": "(610) 387-5172"
}

ans = input("What do you want to know?: ").lower()

## Option-1
if ans in person.keys():
    print(person[ans])
else:
    print("I don't have that information.")

## Option-2
print( person.get(ans, "aI don't have that information.") )