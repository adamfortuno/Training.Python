#!/usr/bin/env python3

import requests, json, html
import pprint as pp

wants_question = True
url = 'https://opentdb.com/api.php?amount=1&category=14&difficulty=medium'

while wants_question == True:
    response = requests.get(url)    

    if response.status_code == 200:
        card = json.loads(response.text)
        print(card)
        question = html.unescape(card['results'][0]['question'])
        answer = card['results'][0]['correct_answer']
        
        guess = input(f"{question}: ")
        thinger = "You guessed right!" if guess == answer else "Incorrect."
            
        play_again = input(f"{thinger} Would you like to play again? [Yes/No]: ")
        wants_question = play_again.lower().strip() == 'yes'
    else:
        print("There was a problem retrieving the question.")
        wants_question = False