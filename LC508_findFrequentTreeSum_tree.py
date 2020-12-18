"""
508. Most Frequent Subtree Sum
Medium: Tree, DFS

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.
Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        c = Counter()
        self.dfs(root, c)
        maxCount = max(c.values())
        return [s for s in c if c[s] == maxCount]
        
    def dfs(self, node, c):
        if node is None: return 0
        s = node.val + self.dfs(node.left, c) + self.dfs(node.right, c)
        c[s] += 1
        return s