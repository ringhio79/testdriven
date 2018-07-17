from byotest import *

# Given an amount of change that needs to be paid, we want to generate the list of coins that should be given to the customer. 

# Our function should pay the minimum number of coins possible, and the available coin denominations are:
 
# 200, 100, 50, 20, 10, 5, 2, and 1.

eur_coins = [200, 100, 50, 20, 10, 5, 2, 1]
us_coins = [200, 100, 50, 25, 10, 5, 2, 1]
gbp = [200, 100, 50, 20, 10, 5]

def make_change(amount, coins = eur_coins):
    change = []
    for coin in coins:
        # if coin > amount:
        #     continue
        while coin <= amount:
            change.append(coin)
            amount = amount - coin
            
    return change
    
    
assert_equal(make_change(0), [])
assert_equal(make_change(50), [50]) 
assert_equal(make_change(13), [10, 2, 1])
assert_equal(make_change(1000), [200, 200, 200, 200, 200])

assert_equal(make_change(59, us_coins), [50, 5, 2, 2])



print("All tests pass")