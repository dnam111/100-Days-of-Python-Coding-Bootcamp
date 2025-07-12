import art
print(art.logo)
print("\n"*5)
Bid = {}
new_bid = True
#Each person's name would be key and bid would be value
# TODO-1: Ask the user for input
def finding_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The highest bidder is {winner} with a bid amoutn of {highest_bid} dollars")
while new_bid:
    name = input("What's your name: ")
    price = int(input("What's your bid amount: "))
# TODO-2: Save data into dictionary {name: price}
    Bid[name] = price
# TODO-3: Whether if new bids need to be added
    should_continue = input("Are there new bids that needs to be added? Type yes or no: ").lower()
    if should_continue == "no":
        new_bid = False
        finding_highest_bidder(Bid)
# TODO-4: Compare bids in dictionary