class Solution:
    def countSubstrings(self, s: str) -> int:
        
        cnt = 0
        memo = [[ True if i == j else False for j in range(len(s))] for i in range(len(s))]
        N = len(s)
        cnt = N
        for i in range(N - 2, -1, -1):
            for j in range(i + 1, N):
                if s[i] == s[j] and (memo[i + 1][j - 1] or (j - i) <= 2):
                    cnt += 1
                    memo[i][j] = True

sln = Solution()
sln.countSubstrings("aaaaaa")
