from collections import deque
     queue = deque([root])
      level = [1]
       while queue:
            new_q = deque()
            curr_level_c = 0
            while queue:
                node = queue.popleft()
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)

            level.append(len(new_q))
            queue = new_q

        return max(level)
