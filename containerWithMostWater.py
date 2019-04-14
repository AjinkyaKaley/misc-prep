class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        maxArea = -1
        area = -1
        left = 0
        right = len(height) - 1

        while left < right:
            base = right - left
            h = min(height[left], height[right])
            area = base * h
            if area > maxArea:
                maxArea = area
            
            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return maxArea

sln = Solution()
print(sln.maxArea([1,8,6,2,5,4,8,3,7]))