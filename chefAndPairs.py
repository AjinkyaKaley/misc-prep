class ChefAndPairs:


# Given an array A of size N, count number of pairs of index i, j such that Ai is even, Aj is odd and i < j
    def chefandpairs(self,nums):
        # 1 2 1 3
        # 5 4 1 2 3
        # 2
        count=0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                for j in range(i+1, len(nums)):
                    if nums[j] % 2 != 0:
                        count += 1
        print(count)

if __name__ == "__main__":
    sln = ChefAndPairs()
    sln.chefandpairs([2,4,6])
    sln.chefandpairs([5,4,1,2,3])
