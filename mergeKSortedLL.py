# Definition for singly-linked list.    
import heapq
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        head = None
        tail = None
        
        k = len(lists)
        heapifyList = [(n.val, n) for n in lists if n]
        heapq.heapify(heapifyList)
        while heapifyList:
            elem = heapq.heappop(heapifyList)
            
            if elem[1] != None:
                heapq.heappush(heapifyList,(elem[0],elem[1]))
            
            if head == None:
                temp = ListNode(elem[0])
                temp.next =elem[1]
                head = temp
                tail = temp
            else:
                temp2 = ListNode(elem[0])
                temp2 = elem[1]
                tail = temp2
                tail = tail.next
        return head

head1 = ListNode(1)
node12 = ListNode(4)
node13 = ListNode(5)
head1.next = node12
node12.next = node13
head2 = ListNode(1)
node22 = ListNode(3)
node23 = ListNode(4)
head2.next = node22
node22.next = node23
head3 = ListNode(2)
node31 = ListNode(6)
head3.next = node31
ll = [head1, head2, head3]
sln = Solution()
sln.mergeKLists(ll)
