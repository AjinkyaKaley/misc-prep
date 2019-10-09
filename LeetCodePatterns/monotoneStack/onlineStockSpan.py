class Solution:

    def onlineStockPrice(self, price):
        stack = []
        solution = [1] * len(price)

        for idx, val in enumerate(price):
            while stack and price[stack[-1]] < val:
                _p = stack.pop()
                solution[_p] += idx - _p
            stack.append(idx)
        return solution

sln = Solution()
print(sln.onlineStockPrice([100, 80, 60, 70, 60, 75, 85]))
