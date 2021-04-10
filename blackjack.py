import random
import time
def sleep(sleep_time):
    time.sleep(sleep_time)


start_loop = True

start = input("Do you want to play blackjack? (y/n)")
if start == "n":
    exit("n == start")
elif start == "y":
    print("Ok!")
    time.sleep(0.2)
    start_loop == False
else:
    print("Thats invalid!")
    time.sleep(0.2)
    exit
computer_cards = random.randint(17, 24)  # The computers total
cards_part_a = random.randint(1,10)  # 2 parts of the "cards" var, used to auto check for aces
cards_part_b = random.randint(1,10) 
if cards_part_a == 1:
    if cards_part_b + 11 <= 21:
        cards_part_a = 11
if cards_part_b == 1:
    if cards_part_a + 11 <= 21:
        cards_part_b = 11
cards = cards_part_a + cards_part_b
win_or_lose = False  # Is the game over?
print("You have:", cards)
while win_or_lose == False:
    hit_or_stay = input("Hit or stay? (h/s)")
    if hit_or_stay == "h":
        cards = cards + random.randint(1,10)
        if cards > 21:
            print("You lose! You were:", cards - 21, "over 21!")
            win_or_lose = True  # The game finished
        print("You have:", cards)
    elif hit_or_stay == "s":
        if cards > 21:
            print("You lose! You were:", cards - 21, "over21!")
            win_or_lose = True
        elif computer_cards > 21:
            print("You win! The computer was", computer_cards - 21, "over 21!")
            win_or_lose = True
        elif cards > computer_cards:
            print("You win! Your number was:", cards-computer_cards, "over the computer's number!")
            win_or_lose = True
        elif cards < computer_cards:
            print("You lose! You number was:", computer_cards-cards, "under the computer's number!")
            win_or_lose = True
        elif cards == computer_cards:
            print("Draw! Your number and the computer's number were both:", cards)
            win_or_lose == True
    elif hit_or_stay != "s":
        exit("invalid lol")
print("Ending...")
input("Press any button to end...")
exit