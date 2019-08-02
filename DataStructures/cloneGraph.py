"""
# Definition for a Node.
"""

class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

import collections
import copy
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        queue = collections.deque()
        queue.append(node)
        lookup = collections.defaultdict(lambda: None)
        clonehead = Node(node.val, [])
        lookup[node]=clonehead

        while queue:
            _node = queue.popleft()
            cloneNode = lookup[_node]

            for v in _node.neighbors:
                cloneV = lookup[v]
                if cloneV:
                    cloneNode.neighbors.append(cloneV)
                else:
                    temp = Node(v.val, [])
                    lookup[v] = temp
                    cloneNode.neighbors.append(temp)
                    queue.append(v)

        return clonehead

sln = Solution()
head = Node(1,[])
two = Node(2,[])
three = Node(3,[])
four = Node(4,[])

head.neighbors = [two, four]
two.neighbors = [head, three]
three.neighbors = [two, four]
four.neighbors = [head, three]
x=sln.cloneGraph(head)
print(x)
