class Solution:

    def generate(self, numRows: int):
        result = [[] for i in range(numRows)]
        result[0].append(1)
        result[1].append(1)
        result[1].append(1)

        for row in range(2, numRows):
            for j in range(0, row+1):
                if j == 0 or j == row:
                    result[row].append(1)
                else:
                    result[row].append(result[row-1][j-1]+result[row-1][j])

        return result[numRows - 1]

sln = Solution()
sln.generate(5)