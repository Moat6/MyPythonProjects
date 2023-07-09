import os

print(f"Welcome to auction bidder")
bidders={}
while True:
    name=input("Enter name of the bidder :")
    bid=int(input("Enter the bidding amount :"))
    bidders[name]=bid
    new=input("Are there more bidders? (y/n) :")
    if new=="y" :
        os.system("cls")
        continue
    else :
        break
for name in bidders :
    highest_bid=0
    winner=None
    if bidders[name]>highest_bid :
        highest_bid=bidders[name]
        winner=name

print(f"Highest Bidder is {winner} with bid of {highest_bid}")