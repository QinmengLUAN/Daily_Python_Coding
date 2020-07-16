"""
429. N-ary Tree Level Order Traversal
Medium: BFS, iterative, O(N)

Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        curr_layer, res = [], []
        curr_layer.append(root)
        
        while curr_layer:
            tmp = []
            next_layer = []
            for node in curr_layer:
                tmp.append(node.val)
                for child in node.children:
                    next_layer.append(child)
            res.append(tmp)
            curr_layer = next_layer
        return res