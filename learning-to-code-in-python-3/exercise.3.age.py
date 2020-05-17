#!/usr/bin/env python3

my_age = 41

their_age = int(input("What's your age?: "))

if (my_age > their_age):
    response = "I'm older than you!"
elif (my_age < their_age):
    response = "You're older than me!"
else:
    response = "We're the same age!"

print(response)