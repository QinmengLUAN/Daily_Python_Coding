"""
337. House Robber III
Medium: DP + cache

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.helper(root, True, {})
    
    def helper(self, node, can_rob, cache):
        if node == None:
            return 0
        
        if can_rob == True:
            if node in cache:
                return cache[node]
            cache[node] = max(node.val + self.helper(node.left, False, cache) + self.helper(node.right, False, cache), self.helper(node.left, True, cache) + self.helper(node.right, True, cache))
            return cache[node]
        else:
            return self.helper(node.left, True, cache) + self.helper(node.right, True, cache)