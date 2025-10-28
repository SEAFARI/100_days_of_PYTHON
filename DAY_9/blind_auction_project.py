import art
print(art.logo)

bidders = {}
keep_bidding = "yes"

def find_highest_bidder():
    max_bid_value = 0
    max_bid_user = ""
    for user in bidders:
        bid_value = bidders[user]
        if bid_value > max_bid_value:
            max_bid_value = bid_value
            max_bid_user = user
    print(f"The max bid value is: {max_bid_value} by {max_bid_user}")

while keep_bidding.lower() == "yes":
    user_name = input("What is your name?:  ")
    user_bid_value = int(input("What is your bid?: $"))
    bidders[user_name] = user_bid_value
    keep_bidding = input("Are there any other bidders? Type 'yes' or 'no' ")
    if keep_bidding.lower() == "yes":
        print("\n"*20)

find_highest_bidder()