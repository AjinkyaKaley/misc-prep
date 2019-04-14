# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        
#         if head == None:
#             return n
        
#         self.removeNthFromEnd(head.next)
#         n -= 1
#         if n == 0:
#             temp = head.next
#             head.next