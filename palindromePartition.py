import copy

class Solution:

    def __init__(self):
        self.allPart = []
        self.currPart = []

    def isPalindrome(self, s, low, high):
        
        while low<high:
            if s[low] != s[high]:
                return False
            low+=1
            high-=1
        return True

    def partition(self, allPart, currPart, start, n, s):
        if start >= n:
            allPart.append(copy.deepcopy(currPart))
            # print(allPart)
            return allPart
        
        for i in range(start,n):
            if self.isPalindrome(s, start, i):
                currPart.append(s[start: i+1])
                self.partition(allPart, currPart, i+1, n, s)
                del currPart[-1]
        return allPart

sln = Solution()

s = 'nitin'
# sln.createSubStr(s,0,len(s))

print(sln.partition(sln.allPart, sln.currPart, 0,len(s), s))
