class Solution:
    def earliestAcq(self, logs, N):
            uf = {x: x for x in range(N)}
            self.groups = N

            def merge(x, y):
                x, y = find(x), find(y)
                if x != y:
                    self.groups -= 1
                    uf[x] = y

            def find(x):
                if uf[x] != x:
                    uf[x] = find(uf[x])
                return uf[x]

            for t, x, y in sorted(logs):
                merge(x, y)
                if self.groups == 1:
                    return t
            return -1

sln = Solution()
sln.earliestAcq([[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], [
                20190224, 2, 4], [20190301, 0, 3], [20190312, 1, 2], [20190322, 4, 5]], N=6)
