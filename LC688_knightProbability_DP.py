"""
688. Knight Probability in Chessboard
Medium: DP

On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

 
Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.

Note:

N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.
"""
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        p = {(r,c): 1}
        for _ in range(K):
            p = {(r, c): sum(p.get((r+i, c+j), 0) for x in (1, 2) for i in (x, -x) for j in (3-x, x-3)) / 8 for r in range(N) for c in range(N)}
        return sum(p.values())

class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        next_pos = [[-1, -2], [-1, 2], [1, -2], [1, 2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
        dp = [[0 for i in range(N)] for i in range(N)]
        dp[r][c] = 1

        for _ in range(K):
            dp_temp = [[0 for i in range(N)] for i in range(N)]
            for i in range(N):
                for j in range(N):
                    for pos in next_pos:
                        nr, nc = i - pos[0], j - pos[1]
                        if (nr >= 0 and nr < N and nc >= 0 and nc < N):
                            dp_temp[i][j] += dp[nr][nc] * 0.125
            dp = dp_temp

        res = 0.0
        for i in range(N):
            for j in range(N):
                res += dp[i][j]
        return res