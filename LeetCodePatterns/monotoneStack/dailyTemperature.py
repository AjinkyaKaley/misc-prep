class Solution:
    def dailyTemperatures(self, T):

        stack = []
        solution = [0] * len(T)
        for idx, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                query_temp_idx = stack.pop()
                solution[query_temp_idx] = idx - query_temp_idx
            stack.append(idx)
        return solution

sln = Solution()
print(sln.dailyTemperatures(T=[73, 74, 75, 71, 69, 72, 76, 73]))
