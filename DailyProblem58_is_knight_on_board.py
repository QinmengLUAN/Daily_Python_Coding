"""
Hi, here's your problem today. This problem was recently asked by Google:

A chess board is an 8x8 grid. Given a knight at any position (x, y) and a number of moves k, we want to figure out after k random moves by a knight, the probability that the knight will still be on the chessboard. Once the knight leaves the board it cannot move again and will be considered off the board.

Here's some starter code:

def is_knight_on_board(x, y, k, cache={}):
  # Fill this in.

print is_knight_on_board(0, 0, 1)
# 0.25
"""
# There are 8 different positions from where the Knight can reach to (x,y) in one step, 
# and they are: (x+1,y+2), (x+2,y+1), (x+2,y-1), (x+1,y-2), (x-1,y-2), (x-2,y-1), (x-2,y+1), (x-1,y+2). 


def is_knight_on_board(x, y, k, cache={}):
  # Fill this in.
  N = 8
  next_pos = [[-1, -2], [-1, 2], [1, -2], [1, 2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
  dp = [[0 for i in range(N)] for i in range(N)]
  dp[x][y] = 1

  for _ in range(k):
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

print(is_knight_on_board(0, 0, 1))
# 0.25