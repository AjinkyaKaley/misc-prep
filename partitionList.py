# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int):
        if head is None:
            return head
            
        leftList = ListNode(0)
        rightList = ListNode(0)
        headOfLL = leftList
        headOfRL = rightList

        while head is not None:
            if head.val < x:
                leftList.next = ListNode(head.val)
                leftList = leftList.next
            elif head.val > x:
                rightList.next = ListNode(head.val)
                rightList = rightList.next
            head = head.next
        leftList.next =  ListNode(x)
        leftList = leftList.next
        leftList.next =  headOfRL.next
        return headOfLL.next
        
sln = Solution()
l1 = ListNode(1)
l2 = ListNode(4)
l3 = ListNode(3)
l4 = ListNode(2)
l5 = ListNode(5)
l6 = ListNode(2)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

sln.partition(l1,3)