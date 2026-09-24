import art
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

continuation = True
allbids = {}
print(art.logo)
while continuation:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    allbids[name] = bid
    confirmation = input("Are there any other bidders? Type 'yes' or 'no': ")
    print('\n' * 100)
    if confirmation == 'yes':
        continuation = True
    elif confirmation == 'no':
        continuation = False
    else:
        print("Invalid Input")
        confirmation = input("Are there any other bidders? Type 'yes' or 'no': ")
highestkey = max(allbids, key=allbids.get)
highestvalue = allbids[highestkey]
print(f"The winner is {highestkey} with a bid of ${highestvalue}")





