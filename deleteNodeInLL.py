# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        self.count = n

        def helper(head, count):
            if head.next:
                root = helper(head.next, count)
                self.count -= 1
                if self.count == 0:
                    head.next = root.next
            return head

        r = helper(head, n)
        if self.count == 1:
            r = r.next
        return r
head = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
sln = Solution()
sln.removeNthFromEnd(head,5)
