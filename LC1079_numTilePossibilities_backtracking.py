"""
1079. Letter Tile Possibilities
Medium: Backtracking

You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
"""
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        self.helper(tiles, "", res)
        # print(res)
        return len(res)
    
    def helper(self, t, st, res):
        # print(res)
        if len(st) > 0:
            res.add(st)
        for i in range(len(t)):
            st += t[i]
            self.helper(t[:i] + t[i+1:], st, res)
            st = st[:-1]