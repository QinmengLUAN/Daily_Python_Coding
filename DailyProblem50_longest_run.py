"""
Hi, here's your problem today. This problem was recently asked by Microsoft:

Return the longest run of 1s for a given integer n's binary representation.

Example:
Input: 242
Output: 4
242 in binary is 0b11110010, so the longest run of 1 is 4.

def longest_run(n):
  # Fill this in.

print longest_run(242)
# 4
"""
"""
Bit manipulation:
      11101111   (x)
    & 11011110   (x << 1)
    ----------
      11001110   (x & (x << 1)) 
        ^    ^
        |    |
   trailing 1 removed
"""
# Expected Time Complexity: O(log N).
# Expected Auxiliary Space: O(1).
def longest_run(n):
    cnt = 0
    # Count the number of iterations to 
    # reach x = 0. 
    while n != 0:
        n = n & (n << 1)
        cnt += 1
    return cnt

print(longest_run(242))
# 4