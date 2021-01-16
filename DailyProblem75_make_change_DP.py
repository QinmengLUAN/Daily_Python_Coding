"""
Hi, here's your problem today. This problem was recently asked by Uber:

Given a list of possible coins in cents, and an amount (in cents) n, return the minimum number of coins needed to create the amount n. If it is not possible to create the amount using the given coin denomination, return None.

Here's an example and some starter code:

def make_change(coins, n):
  # Fill this in.
  
print(make_change([1, 5, 10, 25], 36))
# 3 coins (25 + 10 + 1)
"""
# recursion
import sys
def make_change1(coins, n):
    # base case
    m = len(coins)
    if (n == 0):
        return 0
 
    # Initialize result
    res = sys.maxsize
     
    # Try every coin that has smaller value than V
    for i in range(0, m):
        if (coins[i] <= n):
            sub_res = make_change(coins, n-coins[i])
 
            # Check for INT_MAX to avoid overflow and see if
            # result can minimized
            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1
 
    return res

# A Dynamic Programming based Python3 program to 
# find minimum of coins to make a given change V
import sys 
 
# m is size of coins array (number of 
# different coins)
def make_change(coins, V):
     
    # table[i] will be storing the minimum 
    # number of coins required for i value. 
    # So table[V] will have result
    table = [0 for i in range(V + 1)]
    m = len(coins)
 
    # Base case (If given value V is 0)
    table[0] = 0
 
    # Initialize all table values as Infinite
    for i in range(1, V + 1):
        table[i] = sys.maxsize
 
    # Compute minimum coins required 
    # for all values from 1 to V
    for i in range(1, V + 1): 
        # Go through all coins smaller than i
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and
                    sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
    return table[V]
  
print(make_change([1, 5, 10, 25], 36))
# 3 coins (25 + 10 + 1)