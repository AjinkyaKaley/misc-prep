#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        frontPtr = head.next
        backPtr = head

        while backPtr!=None and frontPtr!=None:
            temp = frontPtr.val
            frontPtr.val = backPtr.val
            backPtr.val = temp

            backPtr = frontPtr.next
            if backPtr != None:
                frontPtr = frontPtr.next.next

    def printLL(self, head):
        while head!=None:
            print(head.val)
            head = head.next

head = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

# ListNode l2 = ListNode(2)
head.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

sln = Solution()
# sln.printLL(head)

sln.swapPairs(head)
sln.printLL(head)
                