class Solution:

    def wordTypying(self, sentence, rows, cols):
        from collections import deque
        queue = deque(reversed(sentence))
        count = 0
        for i in range(rows):
            j = 0
            sent=""
            while j + len(queue[-1]) <= cols:
                word = queue.pop()
                sent += word + " "
                j += len(word)
                j += 1
                queue.appendleft(word)
            print(sent)

sln = Solution()
sln.wordTypying(['I', 'had', 'apple', 'pie'], 4, 5)
# sln.wordTypying(['Hello','world'], 2, 8)