import copy
from collections import deque

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        visited = set()
        totalResult = []
        self.result = float("inf")

        def helper(beginWord, endWord, visited, wordList, currentSolution):
            if beginWord == endWord:
                totalResult.append(copy.deepcopy(currentSolution))
                self.result = min(len(currentSolution),self.result)
                return

            def countDiff(x):
                countDiff = 0
                if len(x) == len(beginWord) or x != beginWord:
                    i = 0
                    while i < len(beginWord):
                        if beginWord[i] != x[i]:
                            countDiff += 1
                        i += 1
                return countDiff == 1 and x not in visited

            candidates = list(filter(countDiff, wordList))

            for wc in candidates:
                visited.add(wc)
                currentSolution.append(wc)
                helper(wc, endWord, visited, wordList, currentSolution)
                visited.remove(wc)
                del currentSolution[-1]

        helper(beginWord, endWord, visited, wordList,[])
        return self.result+1

    def ladderLength(self, beginWord, endWord, wordList):
        queue = [(beginWord, 1)]
        visited = set()

        while queue:
            word, dist = queue.pop(0)
            if word == endWord:
                return dist
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = word[:i] + j + word[i+1:]
                    if tmp not in visited and tmp in wordList:
                        queue.append((tmp, dist+1))
                        visited.add(tmp)
        return 0

    def ladderLengthOptimal(self, beginWord, endWord, wordList):

        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d

        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0

        d = construct_dict(wordList)
        return bfs_words(beginWord, endWord, d)
sln = Solution()
res = sln.ladderLengthOptimal(
    "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
print(res)
# for r in res:
#     print(r)
