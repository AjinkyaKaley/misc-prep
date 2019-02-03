# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#2 4 3 8
#5 6 4
#7 0 8 8
class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        r = None
        carry = 0
        while l1 != None and l2 != None:
            total = l1.val + l2.val + carry
            carry = total // 10
            if total >= 10:
                digit = total % 10
            else:
                digit = total
            
            if r is None:
                r = ListNode(digit)
                result_ll = r
            else:
                r.next = ListNode(digit)
                r = r.next
            l1 = l1.next
            l2 = l2.next

        if l1 is None and l2 is None and carry != 0:
            r.next = ListNode(carry)
            return result_ll

        tempL1 = None
        tempL2 = None
        if l1 is None and l2 is not None:
            print("l2 > l1: "+str(l2.val))
            tempL1 = l2
            tempL2 = l1
        else:
            print("l1 > l2: "+str(l1.val))
            tempL1 = l1
            tempL2 = l2
        # longllHead = r
        if tempL1 is not None and tempL2 is None:
            while tempL1 is not None:
                total = tempL1.val + carry
                carry = total // 10
                if total >= 10:
                    digit = total % 10
                else:
                    digit = total
                r.next = ListNode(digit)
                r = r.next
                tempL1 = tempL1.next
            if tempL1 is None and carry != 0:
                r.next = ListNode(carry)
            
        return result_ll

    def reverseLinkedList(self, ll):
        if ll == None:
            return ll
        self.reverseLinkedList(ll.next)
        print(str(ll.val), end="", flush=True)
        

sln = Solution()
l1 = ListNode(1)
l2 = ListNode(4)
l3 = ListNode(3)
m1 = ListNode(9)
m2 = ListNode(9)
m3 = ListNode(4)
m4 = ListNode(8)

# l1.next = l2
# l2.next = l3
# l3.next = m4
m1.next = m2
# m2.next = m3
# m3.next = m4
result = sln.addTwoNumbers(l1,m1)
sln.reverseLinkedList(result)
print()