class Solution(object):

    def uniqueLetterString(self, S):
        import collections
        index = collections.defaultdict(list)
        for i, c in enumerate(S):
            index[c].append(i)

        ans = 0
        for A in index.values():
            A = [-1] + A + [len(S)]
            for i in range(1, len(A) - 1):
                ans += (A[i] - A[i-1]) * (A[i+1] - A[i])
        return ans % (10**9 + 7)

sln = Solution()
sln.uniqueLetterString("LETTER")
