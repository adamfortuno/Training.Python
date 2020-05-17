#!/usr/bin/env python3

import time as time
import matplotlib.pyplot as plt
import random as random

counter = 1
succeeded = 0
failed = 0
words = 'pennsylvania computer dinosuar trivial thymus'.split()
word = random.choice(words)
duration = []

print(f"Your word is '{word}'")

while counter <= 5:
    start = time.time()
    attempt = input(f"Try #{counter}: ")
    finish = time.time()

    duration.append(finish - start)
    
    if attempt == word:
        succeeded += 1
    else:
        failed += 1

    counter += 1

print("Results:")
print(f"--Correct: {succeeded}")
print(f"--Missed:  {failed}")

x = list(range(1, 6))
y = duration
legend = ["First", "Second", "Third", "Fourth", "Fifth"]
plt.xticks(x, legend)
plt.plot(x, y)
plt.ylabel('Time (s)')
plt.xlabel('Attempts')
plt.show()