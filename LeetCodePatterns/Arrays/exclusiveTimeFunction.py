class Solution:
    def exclusiveTime(self, n: int, logs):
        stack = []
        solution = []
        lookup = {}
        for i, log in enumerate(logs):
            func_id, state_idf, ts = log.split(":")
            if state_idf == "start":
                stack.append(func_id)
                lookup[func_id] = i
            elif state_idf == "end":
                stack.pop()
                solution.append(i - lookup[func_id])

        return solution

sln = Solution()
sln.exclusiveTime(n=2, logs=["0:start:0", "1:start:2", "1:end:5", "0:end:6"])
