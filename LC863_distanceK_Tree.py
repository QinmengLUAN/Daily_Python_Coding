"""
863. All Nodes Distance K in Binary Tree
Medium: Tree, Recursion

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.



Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if root == None:
            return []
        if K == 0:
            return [target.val]
        parents = []
        self._dfs(root, target, parents)
        res = []
        for i in range(len(parents)):
            # print(parents[i].val)
            if K - i == 0:
                res.append(parents[i].val)
                break
            if i == 0:
                self._find_distance(parents[i].right, K-i-1, res)
                self._find_distance(parents[i].left, K-i-1, res)
            else:
                if parents[i].left == parents[i-1]:
                    self._find_distance(parents[i].right, K-i-1, res)
                else:
                    self._find_distance(parents[i].left, K-i-1, res)
        return res
    
    def _dfs(self, node, target, parents):
        if not node:
            return False
        if node == target or self._dfs(node.left, target, parents) or self._dfs(node.right, target, parents):
            parents.append(node)
            return True
        else:
            return False
    def _find_distance(self, node, distance, res):
        if not node:
            return
        if not distance:
            res.append(node.val)
        else:
            self._find_distance(node.left, distance-1, res)
            self._find_distance(node.right, distance-1, res)