"""
Hi, here's your problem today. This problem was recently asked by AirBNB:

Given a linked list and a number k, rotate the linked list by k places.

Here's some starter code and an example:

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    current = self
    ret = ''
    while current:
      ret += str(current.value)
      current = current.next
    return ret

def rotate_list(list, k):
  # Fill this in.

# Order is 1, 2, 3, 4
llist = Node(1, Node(2, Node(3, Node(4))))

# Order should now be 3, 4, 1, 2
print(rotate_list(llist, 2))
# 3412
"""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    current = self
    ret = ''
    while current:
      ret += str(current.value)
      current = current.next
    return ret

def rotate_list(llist, k):
  # Fill this in.
  length = 1
  node = llist
  while node.next:
    length += 1
    node = node.next
  node.next = llist


  tmp = llist
  cnt  = 1
  while cnt < (length-k):
    tmp = tmp.next
    cnt += 1
  nroot = tmp.next
  tmp.next = None
  return nroot

# Order is 1, 2, 3, 4, 5
llist = Node(1, Node(2, Node(3, Node(4, Node(5)))))

# Order should now be 4, 5, 1, 2, 3
print(rotate_list(llist, 2))
# 45123