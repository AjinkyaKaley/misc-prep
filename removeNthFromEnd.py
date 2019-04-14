# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, trail :'ListNode', head: 'ListNode', n: 'int') -> 'ListNode':

        if head == None:
            return n
        r = self.removeNthFromEnd(head, head.next, n)
        r-=1
        if r == 0:
            if trail is None:
                head = head.next
            else:
                trail.next = head.next
        return r

sln = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5

sln.removeNthFromEnd(None,l1,5)


