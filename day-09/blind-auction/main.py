from .art import logo
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def auction():
    print(logo)
    bids = {}
    while True:
        bidder = input("What is your name?\n")
        bid = int(input("What is your bid?\n$"))
        bids[bidder] = bid
        answer = input("Is there another bid?\n")
        clear()
        if answer.lower() == "no":
            break
    clear()
    highest_bid = 0
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            highest_bidder = bidder
    print(f"{highest_bidder} is the highest bidder with a bid of ${highest_bid}")

auction()
