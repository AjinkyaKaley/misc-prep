class Solution:
    def shortestDistance(self, words, word1: str, word2: str) -> int:

        idx1 = -1
        idx2 = -1
        ans = float("inf")
        for i in range(len(words)):
            if word1 == words[i]:
                idx1 = i
            elif word2 == words[i]:
                idx2 = i
            if idx1 != -1 and idx2 != -1:
                ans = min(ans, abs(idx1-idx2))
        return ans

sln = Solution()
sln.shortestDistance(["practice", "makes", "perfect",
                      "coding", "makes"], "coding", "practice")
