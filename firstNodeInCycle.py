
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        slowPtr = head
        fastPtr = head.next
        
        while fastPtr:
            if slowPtr is fastPtr:
                break
            if slowPtr.next:
                slowPtr = slowPtr.next
            if fastPtr.next:
                fastPtr = fastPtr.next.next
            else:
                return -1
            
        if not fastPtr:
            return -1
        slowPtr = head
        idx=0
        
        while slowPtr != fastPtr:
            idx +=1
            slowPtr = slowPtr.next
        return idx

head = Node(3)
l2 = Node(2)
l3 = Node(0)
l4 = Node(4)
head.next = l2
l2.next = l3
l3.next = l4
l4.next = l2
sln = Solution()
sln.detectCycle(head)