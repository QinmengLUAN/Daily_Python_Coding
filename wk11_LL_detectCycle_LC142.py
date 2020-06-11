"""
142. Linked List Cycle II
Medium: Linked list, Position(nr + l) = Position(l)
Time complexity O(n)--- propotional to the length of the list
Space complexity O(1)

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.


Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow-up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1: slower
class Solution:
    def detectCycle_1(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return None  
        node_f = node_s = head

        # Check if it is a circle
        node_f = node_f.next
        while node_f != node_s:
            if node_f.next == None or node_f.next.next == None:
                return None
            node_f = node_f.next.next
            node_s = node_s.next
        
        node_res1 = node_res2 = head

        # Move node_res1 for r steps       
        node_f = node_f.next
        node_res1 = node_res1.next
        while node_f != node_s:
            node_f = node_f.next
            node_res1 = node_res1.next

        # node_res1 and node_res2 will meet after l steps               
        while node_res1 != node_res2: 
            node_res1 = node_res1.next
            node_res2 = node_res2.next
        
        return node_res1


# Solution 2: faster
# length_fast - lenght_s = nr
# length_fast = 2 * length_s 
# Hence, length_s = nr
# node_res (i.e. head) and node_s will meet after l steps
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        node_s = node_f = head
        while node_f != None and node_f.next != None and node_f.next.next != None:
            node_f = node_f.next.next
            node_s = node_s.next
            if node_f == node_s:
                break
        if node_f == None or node_f.next == None or node_f.next.next == None:
            return None
        
        node_res = head
        while node_res != node_s:
            node_res = node_res.next
            node_s = node_s.next
        return node_res