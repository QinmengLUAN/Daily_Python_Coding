"""
Hi, here's your problem today. This problem was recently asked by Google:

Design a Tic-Tac-Toe game played between two players on an n x n grid. A move is guaranteed to be valid, and a valid move is one placed on an empty block in the grid. A player who succeeds in placing n of their marks in a horizontal, diagonal, or vertical row wins the game. Once a winning condition is reached, the game ends and no more moves are allowed. Below is an example game which ends in a winning condition:

Given n = 3, assume that player 1 is "X" and player 2 is "O" 
board = TicTacToe(3);

board.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

board.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

board.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

board.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

board.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

board.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

board.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|

Here's a starting point:

class TicTacToe(object):
  def __init__(self, n):
    # Fill this in.

  def move(self, row, col, player):
    # Fill this in.

board = TicTacToe(3)
board.move(0, 0, 1)
board.move(0, 2, 2)
board.move(2, 2, 1)
board.move(1, 1, 2)
board.move(2, 0, 1)
board.move(1, 0, 2)
print(board.move(2, 1, 1))
"""
"""
Algo: O(1)
Record the number of moves for each rows, columns, and two diagonals.
For each move, we -1 for each player 1's move and +1 for player 2's move.
Then we just need to check whether any of the recored numbers equal to n or -n.
"""
class TicTacToe(object):
  def __init__(self, n):
    # Fill this in.
    self.row, self.col, self.diag, self.anti_diag, self.n = [0] * n, [0] * n, 0, 0, n

  def move(self, row, col, player):
    # Fill this in.
    offset = 2 * player - 3
    self.row[row] += offset
    self.col[col] += offset

    if col == row:
        self.diag += offset
    if col + row == self.n - 1:
        self.anti_diag += offset
    
    if offset * self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
        return player
    return 0

board = TicTacToe(3)
board.move(0, 0, 1)
board.move(0, 2, 2)
board.move(2, 2, 1)
board.move(1, 1, 2)
board.move(2, 0, 1)
board.move(1, 0, 2)
print(board.move(2, 1, 1))