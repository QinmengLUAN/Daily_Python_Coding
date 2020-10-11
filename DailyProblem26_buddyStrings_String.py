"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:
Input: A = "aa", B = "aa"
Output: true
Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:
Input: A = "", B = "aa"
Output: false
Here's a starting point:

class Solution:
  def buddyStrings(self, A, B):
    # Fill this in.

print Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb')
# True
print Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb')
# False
"""
class Solution:
  def buddyStrings(self, A, B):
    if len(A) != len(B):
        return False
    A_lis = []
    B_lis = []
    for i in range(len(A)):
        if A[i] != B[i]:
            A_lis.append(A[i])
            B_lis.append(B[i])
    if len(A_lis) != 2:
        return False
    if A_lis[0] == B_lis[1] and A_lis[1] == B_lis[0]:
        return True
    return False

print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False