import bisect
class Solution:
    def __init__(self, persons, times):
        self.leads, self.times, count = [], times, {}
        lead = -1
        for t, p in zip(times, persons):
            count[p] = count.get(p, 0) + 1
            if count[p] >= count.get(lead, 0):
                lead = p
            self.leads.append(lead)

    def q(self, t):
        return self.leads[bisect.bisect(self.times, t) - 1]


sln = Solution([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
sln.q(3)
sln.q(12)
sln.q(25)
sln.q(24)
sln.q(8)