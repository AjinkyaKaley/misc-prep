class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        self.head = head

        def helper(tail):
            if tail:
                helper(tail.next)
                if tail.val != self.head.val:
                    return False
                elif self.head is tail:
                    return True
                self.head = self.head.next
        return helper(head)


head = Node(1)
l2 = Node(2)
# l3 = Node(2)
# l4 = Node(1)
# l5 = Node(3)
head.next = l2
# l2.next = l5
# l5.next = l3
# l3.next = l4
sln = Solution()
sln.isPalindrome(head)
{"$id": "1", "next": {"$id": "2", "next": {"$id": "3", "next": {
    "$id": "4", "next": {"$ref": "1"}, "val": 1}, "val": 4}, "val": 2}, "val": 3}

{"$id": "1", "next": {"$id": "2", "next": {"$id": "3", "next": {
    "$id": "4", "next": {"$ref": "1"}, "val": 2}, "val": 1}, "val": 4}, "val": 3}
