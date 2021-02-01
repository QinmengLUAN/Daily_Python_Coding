"""
Hi, here's your problem today. This problem was recently asked by Google:

Given a positive integer, find the square root of the integer without using any built in square root or power functions (math.sqrt or the ** operator). Give accuracy up to 3 decimal points.

Here's an example and some starter code:

def sqrt(x):
  # Fill this in.
  
print(sqrt(5))
# 2.236
"""
def sqrt(x):
    l, r = 1, x
    
    while l < r:
        mid = l + (r - l) / 2
        mul = mid * mid

        if (0.0005 < abs(r - l) < 0.001):
            return round(mid, 3)

        elif mul > x:
            r = mid

        elif mul < x:
            l = mid

        else:
            return round(mid, 3)
  
print(sqrt(5))
# 2.236