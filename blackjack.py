import random
import time


start_loop = True

start = input("Do you want to play blackjack? (y/n)")
if start == "n":
    exit("n == start")
elif start == "y":
    print("Ok!")
    time.sleep(0.2)
    start_loop == False
elif True:
    print("Thats invalid!")
    time.sleep(0.2)
    exit
Computer_number = random.randint(17, 24)
cards_part_a = random.randint(1,10)
cards_part_b = random.randint(1,10)
if cards_part_a == 1:
    if cards_part_b + 11 <= 21:
        cards_part_a = 11
if cards_part_b == 1:
    if cards_part_a + 11 <= 21:
        cards_part_b = 11
cards = cards_part_a + cards_part_b
win_or_lose = False
print("You have:", cards)
while win_or_lose == False:
    hit_or_stay = input("Hit or stay? (h/s)")
    if hit_or_stay == "h":
        cards = cards + random.randint(1,10)
        if cards > 21:
            print("You lose! You were:", cards-21, "over 21!")
            win_or_lose = True
        print("You have:", cards)
    elif hit_or_stay == "s":
        if cards > 21:
            print("You lose! You were:", cards-21, "over21!")
            win_or_lose = True
        elif Computer_number > 21:
            print("You win! The computer was", Computer_number-21, "over 21!")
            win_or_lose = True
        elif cards > Computer_number:
            print("You win! Your number was:", cards-Computer_number, "over the computer's number!")
            win_or_lose = True
        elif cards < Computer_number:
            print("You lose! You number was:", Computer_number-cards, "under the computer's number!")
            win_or_lose = True
        elif cards == Computer_number:
            print("Draw! Your number and the computer's number were both:", cards)
            win_or_lose == True
    elif hit_or_stay != "s":
        exit("invalid lol")
print("End...")
time.sleep(1)
exit