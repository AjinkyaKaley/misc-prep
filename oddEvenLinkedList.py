# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        even = None
        odd = None
        oddHead = None
        evenHead = None

        while head != None:
            if head.val % 2 == 0:
                if even:
                    even.next = head
                    even = even.next
                else:
                    even = head
                    evenHead = head
            else:
                if odd:
                    odd.next = head
                    odd = odd.next
                else:
                    odd = head
                    oddHead = head
            head = head.next
            
        odd.next = evenHead
        temp = oddHead
        while temp:
            print(temp.val)
            temp = temp.next
        return oddHead


head = Node(1)
l2 = Node(2)
l3 = Node(3)
l4 = Node(4)
head.next = l2
l2.next = l3
l3.next = l4
sln = Solution()
sln.oddEvenList(head)
