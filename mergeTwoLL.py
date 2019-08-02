# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        tail = None
        
        while l1 and l2:
            temp = None
            if l1.val < l2.val:
                temp = l1
                l1 = l1.next
            else:
                temp = l2
                l2 = l2.next
                
            if head is None:
                head = temp
                tail = temp
            else:
                tail.next = temp
                tail = tail.next
                
        if l1:
            tail.next = l1
        else:
            tail.next = l2
        return head
        