"""
52. N-Queens II
Hard: Backtracking

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        placed = []
        return self.helper(n, placed)
        
    def helper(self, n, placed):
        r_placed = len(placed)
        if r_placed == n:
            return 1
        
        res = 0
        for c in range(n): # Scan column 0 - 7 on row: r_placed
            ok = True
            for r in range(r_placed): # Check all positions of occupied questions
                if placed[r] == c or abs(c - placed[r]) == abs(r_placed - r):
                    ok = False
                    break
            if ok:
                placed.append(c)
                res += self.helper(n, placed)
                placed.pop()
        return res