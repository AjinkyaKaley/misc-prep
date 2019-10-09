class Solution:

    def palindromeSplit(self,A, B):
        ptr1 = 0
        ptr2 = len(A) - 1
        left = 0
        right = 0
        
        while ptr1 < ptr2:
            if A[ptr1] == A[ptr2]:
                left += 1
            elif B[ptr1] == B[ptr2]:
                right += 1
            ptr1 += 1
            ptr2 -= 1
        if left == right:
            return - 1
        elif left > right:
            return len(A) - left
        return right

sln = Solution()
print(sln.palindromeSplit("qwwe", "abcq"))
print(sln.palindromeSplit("qaxbe", "adadq"))
print(sln.palindromeSplit("qaxbe", "adadq"))
print(sln.palindromeSplit("qaxbe", "abcdf"))


