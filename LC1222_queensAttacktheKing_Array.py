"""
1222. Queens That Can Attack the King
Medium: Array, BFS
On an 8x8 chessboard, there can be multiple Black Queens and one White King.

Given an array of integer coordinates queens that represents the positions of the Black Queens, and a pair of coordinates king that represent the position of the White King, return the coordinates of all the queens (in any order) that can attack the King.

Example 1:
Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
Output: [[0,1],[1,0],[3,3]]
Explanation:  
The queen at [0,1] can attack the king cause they're in the same row. 
The queen at [1,0] can attack the king cause they're in the same column. 
The queen at [3,3] can attack the king cause they're in the same diagnal. 
The queen at [0,4] can't attack the king cause it's blocked by the queen at [0,1]. 
The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0]. 
The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.
Example 2:

Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
Output: [[2,2],[3,4],[4,4]]
Example 3:

Input: queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
Output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]

Check 8 directions around the King.
Find the nearest queen in each direction.
"""
class Solution:
    # BFS1
    def queensAttacktheKing1(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:        
        # queens_set = set((x, y) for x, y in queens)
        queens_set = {(i, j) for i, j in queens}
        res = []
        queens_attack = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1)]

        for m, n in queens_attack:
            i, j = king[0], king[1]
            while 0 <= i < 8 and 0 <= j < 8:
                i, j = i + m, j + n
                if (i, j) in queens_set:
                    res.append([i, j])
                    break
        return res
    # BFS2: shorter version of BFS1 
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        queens_set = set([(x, y) for x, y in queens])
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in range(8):
                    m, n = king[0] + i * k, king[1] + j * k
                    if (m, n) in queens_set:
                        res.append([m, n])
                        break
        return res