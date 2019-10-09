class Solution(object):
    def wordBreak(self, text, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(text) == 0:
            return True
        for i in range(1, len(text)+1):
            word = text[0:i]
            if word in wordDict and self.wordBreak(text[i:], wordDict):
                return True 
        return False


sln = Solution()
lookup = set(["cats", "dog", "and", "cat"])
print(sln.wordBreak('catsanddog', lookup))
