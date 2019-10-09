class Solution:
    def reverseLL(self, head):
        if not head or not head.next:
            return head
        
        p = self.reverseLL(head.next)
        head.next.next = head
        head.next = None
        return p

class lNode:
    def __init__(self,val):
        self.val = val
        self.next = None

head = lNode(1)
l2 = lNode(2)
l3 = lNode(3)
l4 = lNode(4)
l5 = lNode(5)
head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

sln = Solution()
sln.reverseLL(head)