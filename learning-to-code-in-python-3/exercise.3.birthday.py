#!/usr/bin/env python3

months = [
    '_',
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

birth_date = input("What is you birth date [DD-MM-YYYY]?: ")
_, month, _ = birth_date.split('-')
birth_month = int(month)

print(f"You were born in {months[birth_month]}")