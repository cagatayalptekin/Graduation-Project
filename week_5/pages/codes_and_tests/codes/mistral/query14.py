def coin_change(coins, amount):
    # Create a table to store the minimum number of coins for each amount
    table = [float('inf')]* (amount + 1)
    table[0] = 0  # No coins required for an amount of 0

    for i in range(len(coins)):
        for j in range(len(table)):
            if j >= coins[i]:
                table[j] = min(table[j], table[j - coins[i]] + 1)

    # If it's not possible to make up the amount, return -1
    if table[amount] == float('inf'):
        return -1
    else:
        return table[amount]
    
    
# def coin_change(coins, amount):
#     n = len(coins)
    
#     if amount < 0 or (n > 0 and coins[0] > amount):
#         return -1
    
#     dp = [float('inf')] * (amount + 1)
#     dp[0] = 0
    
#     for i in range(1, amount + 1):
#         for c in coins:
#             if i - c >= 0:
#                 dp[i] = min(dp[i], dp[i - c] + 1)
            
#     return dp[-1] if dp[-1] != float('inf') else -1