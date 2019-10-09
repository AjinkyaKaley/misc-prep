class Solution:
    def __init__(self):
        pass

    def union(self,A, B):
        print(A | B)
    
    def intersection(self, A, B):
        print(A & B)
        
    def difference(self, A, B):
        print(A - B)
    
    def symmetricDifference(self, A, B):
        print(A ^ B)
    
sln = Solution()
A = set([1, 2, 3, 4])
B = set([4, 5, 6, 7])
sln.union(A,B)
sln.intersection(A, B)
sln.difference(A, B)
sln.symmetricDifference(A, B)