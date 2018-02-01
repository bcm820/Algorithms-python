
"""
Write a function that takes an amount of money in cents and returns the fewest number of coins possible for the number of cents. Here's an example, given the input 387. Now that you have a few tools at your disposal, the output should be a dictionary, as shown below:
"""

def generate_coin_change(cents):
    coins = {}
    coin_names = ["Quarters", "Dimes", "Nickels", "Pennies"]
    coin_values = [25, 10, 5, 1]
    for i in range(0,4):
        coins[coin_names[i]] = cents / coin_values[i]
        cents = cents % coin_values[i]
    return coins

print(generate_coin_change(43662))