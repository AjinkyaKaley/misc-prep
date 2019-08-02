class Solution:
    lookup = set()
    def distinctSubseqII(self, S,iterResult,lookup):
        
        if iterResult:
            print(''.join(iterResult))
            lookup.add(''.join(iterResult))

        for i in range(len(S)):
            iterResult.append(S[i])
            self.distinctSubseqII(S[i + 1:],iterResult,lookup)
            iterResult.pop()

    def distinctSubseqIIDP(self, S):
        dp = [1]
        last = {}
        for i, x in enumerate(S):
            dp.append(dp[-1] * 2)
            if x in last:
                dp[-1] -= dp[last[x]]
            last[x] = i

        return (dp[-1] - 1) % (10**9 + 7)

sln = Solution()
sln.distinctSubseqII('abab', [], set())

# sln.distinctSubseqIIDP('abab')
# "",
# 0 = "","a"
# 1 = "","a","b","ab"
# 2 = "","a","b","a","ab","aa","ba","aba"
# 3 = "","a","b","a","b","ab","aa","ab","aba","aab","ba","bb","bab","ab","abab"
