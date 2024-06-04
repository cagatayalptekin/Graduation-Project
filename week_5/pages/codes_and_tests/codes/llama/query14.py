# def coin_change(coins, amount):
#     # Initialize a dictionary to keep track of the number of coins of each denomination
#     coin_counts = {}
#     for coin in coins:
#         coin_counts[coin] = 0
    
#     # Find the fewest number of coins required to make up the amount
#     min_coin_count = len(coins)
#     for coin in coins:
#         if amount > coin:
#             min_coin_count += 1
#         else:
#             min_coin_count = min(min_coin_count, coin_counts[coin])
    
#     # Return the minimum number of coins required to make up the amount
#     return min_coin_count



def coin_change(coins, amount):
    # Initialize a dictionary to keep track of the number of coins of each denomination
    denominations = {}
    for coin in coins:
        denominations[coin] = 0
    
    # Loop through all the possible denominations and count how many coins are needed
    for denom in denominations:
        if amount > denominations[denom]:
            return -1 # Not possible to make up that amount with those coins
        else:
            amount -= denominations[denom]
            denominations[denom] = 0 # Subtract the number of coins used so far from the total amount
    return denominations[denom]


# def coin_change(coins, amount):
#     # Initialize two dictionaries: one for the number of coins and another for the total value of the coins
#     num_coins = {}
#     val_coins = {}
#     for coin in coins:
#         if coin not in num_coins:
#             num_coins[coin] = 0
#         num_coins[coin] += 1
#         val_coins[coin] = coin * amount
#     # Find the fewest number of coins required to make up the given amount
#     min_coins = None
#     for coin, count in num_coins.items():
#         if count < amount:
#             if min_coins is None or (min_coins and val_coins[min_coins] > val_coins[coin]):
#                 min_coins = coin
#     return min_coins