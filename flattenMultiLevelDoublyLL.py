"""
# Definition for a Node.
"""

class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        self.result = None
        self.tracker = None
        def helper(head):
            if head:
                if self.result == None:
                    self.result = head
                    self.tracker = self.result
                else:
                    self.tracker.next = head
                    self.tracker = self.tracker.next
                if head.child:
                    temp = head.next
                    temp2 = helper(head.child)
                    head.next = temp2
                    temp2.prev = head
                    runner = temp2.next
                    while runner.next:
                        runner = runner.next
                    runner.next = temp
                    head.child = None
                    return head
                    # head.child = None
                head.next = helper(head.next)
            return head
        helper(head)
        return self.result
        
head = Node(1,None,None,None)
l2 = Node(2, None, None, None)
l3 = Node(3, None, None, None)
l4 = Node(4, None, None, None)
l5 = Node(5, None, None, None)
l6 = Node(6, None, None, None)
l7 = Node(7, None, None, None)
l8 = Node(8, None, None, None)
l9 = Node(9, None, None, None)
l10 = Node(10, None, None, None)
l11 = Node(11, None, None, None)
l12 = Node(12, None, None, None)
head.next = l2
l2.next = l3
l2.prev = head

l3.next = l4
l3.child = l7
l3.prev = l2

l4.next = l5
l4.prev = l3

l5.next = l6
l5.prev = l4

l6.next = None
l6.prev = l5

l7.next = l8
l7.prev = None

l8.next = l9
l8.prev = l7
l8.child = l11

l9.next = l10
l9.prev = l8

l10.next = None
l10.prev = l9

l11.next = l12
l11.prev = l10

l12.next = None
l12.prev = l11


sln = Solution()
sln.flatten(head)

# {"$id": "1", "child": null, "next": {"$id": "2", "child": null, "next": {"$id": "3", "child": null, "next": {"$id": "4", "child": null, "next": {"$id": "5", "child": null, "next": {"$id": "6", "child": null, "next": {"$id": "7", "child": null, "next": {"$id": "8", "child": null, "next": {"$id": "9", "child": null, "next": {"$id": "10", "child": null, "next": {"$id": "11", "child": null, "next": {"$id": "12", "child": null,
#                                                                                                                                                                                                                                                                                                                                                                                                                "next": null, "prev": {"$ref": "11"}, "val": 6}, "prev": {"$ref": "10"}, "val": 5}, "prev": {"$ref": "3"}, "val": 4}, "prev": {"$ref": "8"}, "val": 10}, "prev": {"$ref": "5"}, "val": 9}, "prev": {"$ref": "6"}, "val": 12}, "prev": {"$ref": "5"}, "val": 11}, "prev": {"$ref": "4"}, "val": 8}, "prev": {"$ref": "3"}, "val": 7}, "prev": {"$ref": "2"}, "val": 3}, "prev": {"$ref": "1"}, "val": 2}, "prev": null, "val": 1}
# {"$id": "1", "child": null, "next": {"$id": "2", "child": null, "next": {"$id": "3", "child": null, "next": {"$id": "4", "child": null, "next": {"$id": "5", "child": null, "next": {"$id": "6", "child": null, "next": {"$id": "7", "child": null, "next": {"$id": "8", "child": null, "next": {"$id": "9", "child": null, "next": {"$id": "10", "child": null, "next": {"$id": "11", "child": null, "next": {"$id": "12", "child": null,
#                                                                                                                                                                                                                                                                                                                                                                                                                "next": null, "prev": {"$ref": "11"}, "val": 6}, "prev": {"$ref": "10"}, "val": 5}, "prev": {"$ref": "9"}, "val": 4}, "prev": {"$ref": "8"}, "val": 10}, "prev": {"$ref": "7"}, "val": 9}, "prev": {"$ref": "6"}, "val": 12}, "prev": {"$ref": "5"}, "val": 11}, "prev": {"$ref": "4"}, "val": 8}, "prev": {"$ref": "3"}, "val": 7}, "prev": {"$ref": "2"}, "val": 3}, "prev": {"$ref": "1"}, "val": 2}, "prev": null, "val": 1}

# {"$id": "1", "child": null, "next": {"$id": "2", "child": null, "next": {"$id": "3", "child": null, "next": {"$id": "4", "child": null, "next": {"$id": "5", "child": null, "next": {"$id": "6", "child": null, "next": {"$id": "7", "child": null, "next": {"$id": "8", "child": null, "next": {"$id": "9", "child": null, "next": {"$id": "10", "child": null, "next": {"$id": "11", "child": null, "next": {"$id": "12", "child": null, "next": null, "prev": {"$ref": "11"}, "val": 6}, "prev": {"$ref": "10"}, "val": 5}, "prev": {"$ref": "3"}, "val": 4}, "prev": {"$ref": "8"}, "val": 10}, "prev": {"$ref": "5"}, "val": 9}, "prev": {"$ref": "6"}, "val": 12}, "prev": {"$ref": "5"}, "val": 11}, "prev": {"$ref": "4"}, "val": 8}, "prev": {"$ref": "3"}, "val": 7}, "prev": {"$ref": "2"}, "val": 3}, "prev": {"$ref": "1"}, "val": 2}, "prev": null, "val": 1}
# {"$id": "1", "child": null, "next": {"$id": "2", "child": null, "next": {"$id": "3", "child": null, "next": {"$id": "4", "child": null, "next": {"$id": "5", "child": null, "next": {"$id": "6", "child": null, "next": {"$id": "7", "child": null, "next": {"$id": "8", "child": null, "next": {"$id": "9", "child": null, "next": {"$id": "10", "child": null, "next": {"$id": "11", "child": null, "next": {"$id": "12", "child": null, "next": null, "prev": {"$ref": "11"}, "val": 6}, "prev": {"$ref": "10"}, "val": 5}, "prev": {"$ref": "9"}, "val": 4}, "prev": {"$ref": "8"}, "val": 10}, "prev": {"$ref": "7"}, "val": 9}, "prev": {"$ref": "6"}, "val": 12}, "prev": {"$ref": "5"}, "val": 11}, "prev": {"$ref": "4"}, "val": 8}, "prev": {"$ref": "3"}, "val": 7}, "prev": {"$ref": "2"}, "val": 3}, "prev": {"$ref": "1"}, "val": 2}, "prev": null, "val": 1}
