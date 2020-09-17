"""
Hi, here's your problem today. This problem was recently asked by Apple:

Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

Here is the definition of a node for the tree.

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
  # Fill this in.

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print findCeilingFloor(root, 5)
# (4, 6)
Solution:
https://www.techiedelight.com/floor-ceil-bst-iterative-recursive/
"""
class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findCeilingFloor1(root, key, floor=None, ceil=None):
# Recursive function to find floor and ceil of a given key in a BST
# using a Wrapper
# def findFloorCeil(root, floor, ceil, key):

    # base case
    if root == None:
        return floor.value, ceil.value

    # if node with key's value is found, both floor and ceil is equal
    # to the current node
    if root.value == key:
        return root.value, root.value

    # if given key is less than the root node, recur for left subtree
    elif key < root.value:
        # update ceil to current node before visiting left subtree
        return findCeilingFloor(root.left, key, floor, root)

    # if given key is more than the root node, recur for right subtree
    else:
        # update floor to current node before visiting right subtree
        return findCeilingFloor(root.right, key, root, ceil)

def findCeilingFloor(root, key, floor=None, ceil=None):
    while root:
        if root.value == key:
            floor = ceil = root
            break
        elif root.value > key:
            ceil = root
            root = root.left
        else:
            floor = root
            root = root.right
    return floor.value, ceil.value


root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(findCeilingFloor(root, 5))
# (4, 6)