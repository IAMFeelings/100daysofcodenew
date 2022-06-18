import logo
import os

bidders = {}
finish_bid = False
print(logo.logo)



while finish_bid == False:
    name = input("what's your name? -->")

    bid = int(input("How much will your bid be? -->"))

    bidders[name] = bid

    other_player = input("are there more bidders")

    if other_player == "yes":
        finish_bid = False
    elif other_player == "no":
        finish_bid = True
    else:
        print("wrong input")

temp = 0
name = ""
for key in bidders:
    value = bidders[key]
    if value >= temp:
        temp = value
        name = key


print(f"the highest bider was {name}")



