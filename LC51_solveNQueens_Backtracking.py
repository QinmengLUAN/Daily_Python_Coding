"""
51. N-Queens
Hard

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.


Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queen_pos = self.helper(n, [], [])
        ns = len(queen_pos)
        ans = []
        for i in range(ns):
            res_str = [list(".") * n for i in range(n)]
            for r in range(n):
                c = queen_pos[i][r]
                res_str[r][c] = "Q"
                res_str[r] = "".join(res_str[r])
            ans.append(res_str)
        return(ans)
                 
    def helper(self, n, placed, res):
        if len(placed) == n:
            res.append(placed.copy())
            return
        r = len(placed)
        for c in range(n):
            ok = True
            for nr in range(r):
                if c == placed[nr] or abs(nr - r) == abs(placed[nr] - c):
                    ok = False
                    break
            if ok == True:
                placed.append(c)
                self.helper(n, placed, res)
                placed.pop()
        return res
            