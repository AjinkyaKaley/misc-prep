import collections

from collections import deque


class Solution:
    def slidingPuzzle(self, board):
        neighbours = {0: {1, 3}, 1: {0, 2, 4}, 2: {
            1, 5}, 3: {0, 4}, 4: {3, 1, 5}, 5: {2, 4}}
        seen = set()
        s = "".join(str(board[row][col]) for row in range(
            len(board)) for col in range(len(board[0])))

        queue = deque([(s, s.index("0"), 0)])
        seen.add(s)
        while queue:
            s, pos, depth = queue.popleft()
            seen.add(s)
            if s == "123450":
                return depth
            arr = [c for c in s]
            for nei in neighbours[pos]:
                new_arr = arr[:]
                new_arr[pos], new_arr[nei] = new_arr[nei], new_arr[pos]
                new_s = "".join(new_arr)
                if new_s not in seen:
                    queue.append((new_s, nei, depth+1))

        return -1
# import itertools
# import collections

# class Solution(object):
#     def slidingPuzzle(self, board):
#         R, C = len(board), len(board[0])
#         start = tuple(itertools.chain(*board))
#         queue = collections.deque([(start, start.index(0), 0)])
#         seen = {start}

#         target = (1,2,3,4,5,0)

#         while queue:
#             board, posn, depth = queue.popleft()
#             if board == target:
#                 return depth
#             for d in (-1, 1, -C, C):
#                 nei = posn + d
#                 if abs(nei/C - posn/C) + abs(nei % C - posn % C) != 1:
#                     continue
#                 if 0 <= nei < R*C:
#                     newboard = list(board)
#                     newboard[posn], newboard[nei] = newboard[nei], newboard[posn]
#                     newt = tuple(newboard)
#                     if newt not in seen:
#                         seen.add(newt)
#                         queue.append((newt, nei, depth+1))

#         return -1
sln = Solution()
print(sln.slidingPuzzle([[1, 2, 3], [5, 4, 0]]))
# 4 1 2
# 5 0 3
# 4 1 2 5 0 3
# 0 1 2 3 4 5
# 4 1 2
# 0 5 3

# 1 2 3
# 4 5 0
