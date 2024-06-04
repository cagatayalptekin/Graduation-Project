#Given an integer array `coins` and an integer `amount`, find the fewest number of coins required to make up that amount. If it's not possible to make up that amount, return -1.
def coin_change(coins, amount):
    # Initialize a dictionary to store the minimum number of coins for each amount
    min_coins = {0: 0}

    # Loop through the amounts and find the minimum number of coins required
    for i in range(1, amount + 1):
        min_coins[i] = float('inf')
        for coin in coins:
            if i - coin >= 0 and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1

    # If the amount is not possible to make up, return -1
    if min_coins[amount] == float('inf'):
        return -1

    # Return the minimum number of coins required
    return min_coins[amount]