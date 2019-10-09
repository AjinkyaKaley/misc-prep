"""
BST.

class Node {
	int val
  Node left, right
}

target value t (float number).

find k values in the BST that are closest to the target t

    4
   / \
  2   5
 / \
1   3

k = 2, t = 3.71

[4, 3]

abs value of two node values

"""

from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self._deque = deque()

    def inorderTraversal(self, root, t, k):
        if root:
            self.inorderTraversal(root.left, t, k)
            if not self._deque:
                self._deque.append((abs(t - root.val), root.val))
            elif abs(t - root.val) <= self._deque[-1][0] or len(self._deque) < k:
                self._deque.append((abs(t - root.val), root.val))
            else:
                return
            while len(self._deque) > k:
               self._deque.popleft()
            self.inorderTraversal(root.right, t, k)
    
    # def kClosestValues(self, t, k, root):
    #     # self.inorderTraversal(root)
    #     import heapq
    #     k_closest = []
    #     solution = []
    #     heapq.heapify(k_closest)
    #     for i in range(len(self.inorderResult)):
    #         val = self.inorderResult[i]
    #         diff = abs(t-val)
    #         if k_closest:
    #             if diff < abs(k_closest[0][0]):
    #                 # heapq.heappush(k_closest, (-diff, val))
    #                 heapq.heapreplace(k_closest, (-diff, val))
    #             elif len(k_closest) == k:
    #                 break
    #         else:
    #             heapq.heappush(k_closest,(-diff,val))
            
    
    #     for diff,val in k_closest:
    #         solution.append(val)
        
    #     return solution
    
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

sln = Solution()
sln.inorderTraversal(root, 3.71, 2)
print(sln._deque)

# 12345
# 3.5-1 = 2.5
# 3.5-2 = 1.5
# # 3.5 = 3 = 0.5
# ---XX---
# 3.5-4 = -1.5
# 3.5-5 = -2.5
