# from DataStructures.LinkedListNode import LinkedListNode
# class Solution:

#     def clone(self, head):
#         runner = head

#         while runner:
#             auxNode = LinkedListNode(runner.value, None, None)
#             temp = runner.nextPtr
#             runner.nextPtr = auxNode
#             auxNode.nextPtr = temp
#             runner = runner.nextPtr.nextPtr

#         while head:
#             print(head.value)
#             # resultHead = resultHead.nextPtr

# sln = Solution()
# head = LinkedListNode(1)
# l2 = LinkedListNode(2)
# l3 = LinkedListNode(3)
# l4 = LinkedListNode(4)
# l5 = LinkedListNode(5)
# head.nextPtr = l2
# l2.nextPtr = l3
# l3.nextPtr = l4
# l4.nextPtr = l5

# sln.clone(head)
