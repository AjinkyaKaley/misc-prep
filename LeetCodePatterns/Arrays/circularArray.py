class Solution:

    def prints(self,a, n, ind):
        i = ind

        # print from ind-th index to (n+i)th index.
        while i < n + ind:
            print(a[(i % n)], end=" ")
            i = i + 1


# Driver Code
a = ['A', 'B', 'C', 'D', 'E', 'F']
n = len(a)
sln = Solution()
sln.prints(a, n, 3)