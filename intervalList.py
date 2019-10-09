class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i=0
        j=0
        sol = []
        while i<len(A) and j < len(B):
            lo = max(A[i][0],B[j][0])
            hi = min(A[i][1],B[j][1])
            
            if lo <= hi:
                sol += [[lo,hi]]
            
            if A[i][1] < B[j][1]:
                i+=1
            else:
                j+=1
                
        return sol
sln = Solution()
sln.intervalIntersection(A=[[0, 2], [5, 10], [13, 23], [24, 25]], B=[
                            [1, 5], [8, 12], [15, 24], [25, 26]])
