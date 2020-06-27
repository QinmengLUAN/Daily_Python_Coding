"""
130. Surrounded Regions
Medium: BFS

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nr = len(board)
        if nr == 0:
            return
        nc = len(board[0])
        curr_layer = deque()
        
        for i in [0, nr-1]:
            for j in range(nc):
                self.marking(board, [i,j], curr_layer)
        for j in [0, nc-1]:
            for i in range(nr):
                self.marking(board, [i,j], curr_layer)
        for i in range(nr):
            for j in range(nc):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 1:
                    board[i][j] = 'O'
        return
    def marking(self, board, node, curr_layer):
        [i,j] = node
        if board[i][j] == 'O':
            curr_layer.append([i,j])
            board[i][j] = 1
            while len(curr_layer) > 0:
                next_layer = self.neighbours(board, curr_layer.popleft())
                for m,n in next_layer:
                    if board[m][n] == 'O':
                        board[m][n] = 1
                        curr_layer.append([m, n])
        return
    def neighbours(self, board, node):
        i, j = node
        next_layer = []
        pos = [[i-1,j], [i+1,j], [i, j-1], [i, j+1]]
        for m, n in pos:
            if 0 <= m < len(board) and 0 <= n < len(board[0]):
                next_layer.append([m,n])
        return next_layer