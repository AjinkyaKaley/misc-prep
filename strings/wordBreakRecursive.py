class Solution:

    def wordBreak(self, text, lookup, result):

        for i in range(1, len(text)+1):
            word = text[0:i]
            if word in lookup:
                if i == len(text):
                    result += word
                    print(result)
                    return
                self.wordBreak(text[i:], lookup, result+ word + ' ')

sln = Solution()
lookup = set(["cat", "cats", "and", "sand", "dog"])
sln.wordBreak('catsanddog',lookup, '')
