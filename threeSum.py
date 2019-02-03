class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        i=0
        j=0
        nums.sort()
        results = []

        while i < len(nums) - 2:
            j = i + 1
            k=len(nums) - 1
            while j < k:
                print("I,J,K value: " + str(i)+" ,"+ str(j) +" ,"+ str(k))
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    arr = [nums[i], nums[j], nums[k]]
                    results.append(arr)
                    print(results)
                    # return results
                if sum <= 0:
                    while j+1 < k and nums[j] == nums [j+1]:
                        j+=1
                    j+=1
                if sum >= 0:
                    while j < k-1  and nums[k] == nums[k-1]:
                        k-=1
                    k-=1
            while nums[i] == nums[i+1] and i < len(nums)-2:
                i+=1
            i+=1
            
        return results

sln = Solution()
print(sln.threeSum([-1,0,1,2,-1,4]))
#-1,-1,0,1,2,4