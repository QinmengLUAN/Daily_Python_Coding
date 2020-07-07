"""
19. Remove Nth Node From End of List
Medium: Linked list, Two pointer

Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?

Hint:
Maintain two pointers and update one with a delay of n steps.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def 1(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        f, s = dummy, dummy
        for i in range(n + 1):
            f = f.next
        while f:
            f = f.next
            s = s.next
        temp = s.next.next
        s.next = temp
        return dummy.next