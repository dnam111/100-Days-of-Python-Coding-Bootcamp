import art
print(art.logo)
print("\n"*5)
Bid = {}
new_bid = True
#Each person's name would be key and bid would be value
# TODO-1: Ask the user for input

while new_bid:
    name = input("What's your name: ")
    price = int(input("What's your bid amount: "))
# TODO-2: Save data into dictionary {name: price}
    Bid[name] = price
# TODO-3: Whether if new bids need to be added
    should_continue = input("Are there new bids that needs to be added? Type yes or no: ").lower()
    if should_continue == "no":
        new_bid = False
winning_bidder = max(Bid, key=Bid.get)
print(f"The winner is {winning_bidder} with an amount of {Bid[winning_bidder]} dollars")
# TODO-4: Compare bids in dictionary