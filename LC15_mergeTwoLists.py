"""
Leetcode21. Merge Two Sorted Lists
Easy: Linked list, beginner for this topic, hard to Moe

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # recursively
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        if l1 == None:
            return l2
        if l2 == None:
            return l1       
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        head.next = self.mergeTwoLists(l1, l2)    
        return head
    
    # iteratively
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = temp = ListNode(0)
        while l1 and l2:
            if l1 == None:
                temp.next = l2
            if l2 == None:
                temp.next = l1
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2
        return head.next