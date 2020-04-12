"""
234. Palindrome Linked List
Easy: Linked list, hard to Moe

Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return True
# The section below is used to find the mid node for separating the list
        fast = head
        slow = head
        
        if fast != None and fast.next != None and fast.next.next == None:
            return fast.val == fast.next.val
            
        while fast != None and fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
# The section below is used to deal with the list with even length or odd length            
        if fast.next != None:    
            second_head = slow.next #mid node for the second half of list
            second_head_next = second_head.next       
            second_head.next = None
            slow.next = None
        else:
            second_head = slow #mid node for the second half of list
            second_head_next = second_head.next       
            second_head.next = None
# Reverse the second half list        
        while second_head_next != None: #Reverse the second half of list 
            temp = second_head_next.next
            second_head_next.next = second_head          
            second_head = second_head_next # Pass value to second round reverse
            second_head_next = temp # Pass value to second round reverse     
        # print(head)
        # print(second_head)

# Compare the node.val on first half and second half    
        while head != None and second_head != None and head.val == second_head.val: 
            head = head.next
            second_head = second_head.next
        return head == second_head == None
