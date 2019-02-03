#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    carry=0
    result = None
    finalResult = None

    def countLength(self, l1):
        countl1=0
        while l1 != None:
            countl1 +=1
            l1 = l1.next
        return countl1
        
    def addition(self,l1,l2):
        if l1 is None and l2 is None:
            return
        self.addition(l1.next, l2.next)
        print('l1.val = '+ str(l1.val) + "," 'l2.val = '+ str(l2.val) + "," 'carry = '+str(self.carry))
        total = l1.val + l2.val + self.carry
        digit = total % 10
        self.carry = total // 10
        if self.result is None:
            self.result = ListNode(digit)
            self.finalResult = self.result
        else:
            self.result.next = ListNode(digit)
            self.result = self.result.next

    def printLinkedListReverse(self, ll):
        if ll == None:
            return ll
        self.printLinkedListReverse(ll.next)
        print(str(ll.val), end="", flush=True)

    def additionOfRemainder(self, ll, diff):
        if diff == 0:
            return
        diff -= 1
        self.additionOfRemainder(ll.next, diff)
        print('ll.val = '+ str(ll.val) + "," 'carry = '+str(self.carry))
        total = ll.val + self.carry
        digit = total % 10
        self.carry = total // 10
        self.result.next = ListNode(digit)
        self.result = self.result.next

    def reverseLinkedList(self, llFront, llBack):
        if llBack is None:
            return
        self.reverseLinkedList(llFront, llBack.next)
        holder = llFront.val
        llFront.val = llBack.val
        llBack = holder
        llFront = llFront.next

    def printLinkedList(self,ll):
        if ll is None:
            return
        print(str(ll.val), end="", flush=True)
        self.printLinkedList(ll.next)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1Handle = l1
        l2Handle = l2
        longll = None
        shortll = None
        countl1 = self.countLength(l1Handle)
        countl2 = self.countLength(l2Handle)
        if countl1 < countl2:
            shortll = l1
            longll = l2
        else:
            shortll = l2
            longll = l1

        print('count l1:' + str(countl1))
        print('count l2:' + str(countl2))

        diffForFirstPart = abs(countl1-countl2) 
        diffForSecondPart = diffForFirstPart

        longllHead = longll

        while diffForFirstPart != 0:
            longll = longll.next
            diffForFirstPart -= 1
        self.addition(longll,shortll)
        self.additionOfRemainder(longllHead,diffForSecondPart)
        if self.carry != 0:
            self.result.next = ListNode(self.carry)

        return self.finalResult
        
sln = Solution()
l1 = ListNode(7)
l2 = ListNode(2)
l3 = ListNode(4)
l4 = ListNode(3)

m1 = ListNode(5)
m2 = ListNode(6)
m3 = ListNode(4)

l1.next = l2
l2.next = l3
l3.next = l4
m1.next = m2
m2.next = m3

finalResult = sln.addTwoNumbers(l1,m1)
sln.reverseLinkedList(finalResult, finalResult)
sln.printLinkedList(finalResult)
print()
        
        
