
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        runner = head
        tail = None
        while runner:
            tail = runner
            runner = runner.next
            length += 1
        if k > length:
            k = k % length

        if k == 0:
            return head
        runner = head
        slowRunner = None
        leftSideLen = length - k

        while leftSideLen != 0 and runner:
            slowRunner = runner
            runner = runner.next
            leftSideLen -= 1

        nodesToShuffle = runner
        slowRunner.next = None

        tail.next = head
        # print(nodesToShuffle)
        return nodesToShuffle


head = Node(1)
l2 = Node(2)
l3 = Node(3)
l4 = Node(4)
l5 = Node(5)
# head.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l5
sln = Solution()
sln.rotateRight(head,6)
