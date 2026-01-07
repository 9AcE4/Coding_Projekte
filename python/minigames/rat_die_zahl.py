# Zahlenraten

from random import random

print("Willkommen zum Zahlenratespiel!")
win_number = int(random() * 10) + 1

while True:
    guess = int(input("Rate eine Zahl zwischen 1 und 10: "))

    if guess < win_number:
        print("Die gesuchte Zahl ist größer.")
    elif guess > win_number:
        print("Die gesuchte Zahl ist kleiner.")

    else:
        if guess == win_number:
            print("Herzlichen Glückwunsch! Du hast die richtige Zahl erraten.")
        
            new_game = input("Möchtest du noch einmal spielen? (ja/nein): ")
        
        if new_game == 'ja':
            win_number = int(random() * 10) + 1
            continue
        elif new_game == 'nein':
            break


print("Spiel beendet.")
