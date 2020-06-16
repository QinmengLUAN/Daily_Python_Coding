"""
437. Path Sum III
Easy: Tree
> Solution:
> https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Solution 1:
1. Brute Force: O(nlogn) ~ O(n^2)
1.1 High level walk-through:
(Define return) Define a global var: self.numOfPaths in the main function.
(1st layer DFS) Use recursive traverse to go through each node (can be any order: pre, in, post all fine).
(2nd layer DFS) For each node, walk all paths. If a path sum equals to the target: self.numOfPaths += 1
Return result: return self.numOfPaths
1.2 Complexity analysis
1.2.1 Space
Space complexity is O(1), due to there is no extra cache. However, for any recursive question, we need to think about stack overflow, namely the recursion should not go too deep.
Assume we have n TreeNodes in total, the tree height will vary from O(n) (single sided tree) to O(logn)(balanced tree).
The two DFS will go as deep as the tree height.
1.2.2 Time
Time complexity depends on the two DFS.
1st layer DFS will always take O(n), due to here we will take each node out, there are in total n TreeNodes
2nd layer DFS will take range from O(n) (single sided tree) to O(logn)(balanced tree). This is due to here we are get all the paths from a given node. The length of path is proportional to the tree height.
Therefore, the total time complexity is O(nlogn) to O(n^2).
"""
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # define global return var
        self.numOfPaths = 0
        # 1st layer DFS to go through each node
        self.dfs(root, target)
        # return result
        return self.numOfPaths
    
    # define: traverse through the tree, at each treenode, call another DFS to test if a path sum include the answer
    def dfs(self, node, target):
        # exit condition
        if node is None:
            return 
        # dfs break down 
        self.test(node, target) # you can move the line to any order, here is pre-order
        self.dfs(node.left, target)
        self.dfs(node.right, target)
        
    # define: for a given node, DFS to find any path that sum == target, if find self.numOfPaths += 1
    def test(self, node, target):
        # exit condition
        if node is None:
            return
        if node.val == target:
            self.numOfPaths += 1
            
        # test break down
        self.test(node.left, target-node.val)
        self.test(node.right, target-node.val)

"""
Solution 2
2. Memorization of path sum: O(n)
2.1 High level walk through
In order to optimize from the brutal force solution, we will have to think of a clear way to memorize the intermediate result. Namely in the brutal force solution, we did a lot repeated calculation. For example 1->3->5, we calculated: 1, 1+3, 1+3+5, 3, 3+5, 5.
This is a classical 'space and time tradeoff': we can create a dictionary (named cache) which saves all the path sum (from root to current node) and their frequency.
Again, we traverse through the tree, at each node, we can get the currPathSum (from root to current node). If within this path, there is a valid solution, then there must be a oldPathSum such that currPathSum - oldPathSum = target.
We just need to add the frequency of the oldPathSum to the result.
During the DFS break down, we need to -1 in cache[currPathSum], because this path is not available in later traverse.
Check the graph below for easy visualization.

"""
class Solution(object):
    def pathSum(self, root, target):
        # define global result and path
        self.result = 0
        cache = {0:1}
        
        # recursive to get result
        self.dfs(root, target, 0, cache)
        
        # return result
        return self.result
    
    def dfs(self, root, target, currPathSum, cache):
        # exit condition
        if root is None:
            return  
        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - target
        # update result and cache
        self.result += cache.get(oldPathSum, 0)
        cache[currPathSum] = cache.get(currPathSum, 0) + 1
        
        # dfs breakdown
        self.dfs(root.left, target, currPathSum, cache)
        self.dfs(root.right, target, currPathSum, cache)
        # when move to a different branch, the currPathSum is no longer available, hence remove one. 
        cache[currPathSum] -= 1





        