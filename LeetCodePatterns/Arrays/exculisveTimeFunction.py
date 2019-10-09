class Solution:
    def exclusiveTime(self, n: int, logs):
        stack = []
        solution = [0] * n
        s = logs[0].split(":")
        stack.append(int(s[0]))
        solution[0] = int(s[2])
        i = 1
        prev = int(s[2])
        while i < len(logs):
            s = logs[i].split(":")
            if s[1] == 'start':
                if stack:
                    solution[stack[-1]] += (int(s[2]) - prev)
                stack.append(int(s[0]))
                prev = int(s[2])
            else:
                funcId = stack.pop()
                solution[funcId] += int(s[2]) - prev + 1
                prev = int(s[2]) + 1
            i += 1
        return solution

sln = Solution()
sln.exclusiveTime(2,
                  ["0:start:0", "1:start:2", "1:end:5", "0:end:6"])
