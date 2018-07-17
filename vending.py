from byotest import *

# Given an amount of change that needs to be paid, we want to generate the list of coins that should be given to the customer. 

# Our function should pay the minimum number of coins possible, and the available coin denominations are:
 
# 200, 100, 50, 20, 10, 5, 2, and 1.

coins = [200, 100, 50, 20, 10, 5, 2, 1]


def make_change(amount):
    change = []
    for coin in coins:
        # if coin > amount:
        #     continue
        while coin <= amount:
            change.append(coin)
            amount = amount - coin
            
    return change
    
    
assert_equal(make_change(0), []) 
assert_equal(make_change(13), [10, 2, 1])
assert_equal(make_change(1000), [200, 200, 200, 200, 200])


print("All tests pass")