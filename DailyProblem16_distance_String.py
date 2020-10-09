"""
Hi, here's your problem today. This problem was recently asked by AirBNB:
Leetcode 72

Given two strings, determine the edit distance between them. 
The edit distance is defined as the minimum number of edits 
(insertion, deletion, or substitution) needed to change one string to the other.

For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t).

Here's the signature:

def distance(s1, s2):
  # Fill this in.
         
print distance('biting', 'sitting')
# 2
"""
def distance(word1, word2):
    if word1 == None or word2 == None:
        return -1
    r, c = len(word1), len(word2)
    
    dp = [[0] * (c+1) for i in range(r+1)]
    
    # initialization
    for i in range(r + 1):
        dp[i][0] = i
    for j in range(c + 1):
        dp[0][j] = j
    
    # Transition function:
    # If word1[i] != word[j]:
        # f[i][j] = min(f1, f2, f3)
        # f1 = f[i][j-1] + 1
        # f2 = f[i-1][j] + 1
        # f3 = f[i-1][j-1] +1
    # If word1[i] == word[j]:
        # f[i][j] = f[i-1][j-1]
    
    # Table filling:
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                f1 = dp[i-1][j] + 1
                f2 = dp[i][j-1] + 1
                f3 = dp[i-1][j-1] + 1
                dp[i][j] = min(f1, f2, f3)
    return dp[-1][-1]

print(distance('biting', 'sitting'))
# 2