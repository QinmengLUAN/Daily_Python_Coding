"""
141. Linked List Cycle
Easy：Linked list, Two-pointer

Approach: Two Pointers
Intuition:
Imagine two runners running on a track at different speed. What happens when the track is actually a circle?
Algorithm:
The space complexity can be reduced to O(1) by considering two pointers at different speed - a slow pointer and a fast pointer. 
The slow pointer moves one step at a time while the fast pointer moves two steps at a time.

Given a linked list, determine if it has a cycle in it.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False        
        
        fast = head
        slow = head      
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False