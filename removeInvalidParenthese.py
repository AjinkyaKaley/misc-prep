from collections import Counter
class Solution:
    def removeInvalidParentheses(self, s):
        res = []
        self.visited = set([s])
        self.dfs(s, self.invalid(s), res)
        return res

    def dfs(self, s, n, res):
        if n == 0:
            res.append(s)
            return
        for i in range(len(s)):
            if s[i] in ('(', ')'):
                new_s = s[:i]+s[i+1:]
                if new_s not in self.visited and self.invalid(new_s) < n:
                    self.visited.add(new_s)
                    self.dfs(new_s, self.invalid(new_s), res)

    def invalid(self, s):
        # bracket_counts = Counter(s)
        # return abs(bracket_counts['('] - bracket_counts[')'])
        plus = minus = 0
        memo = {"(": 1, ")": -1}
        for c in s:
            plus += memo.get(c, 0)
            if plus < 0:
                minus += 1
            plus = max(0, plus)
        return plus + minus

sln = Solution()
print(sln.removeInvalidParentheses("()())()s"))
