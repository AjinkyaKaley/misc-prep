import heapq


class headElementStruct:
    def __init__(self, value, array_location, idx_in_array):
        self.value = value
        self.array_location = array_location
        self.idx_in_array = idx_in_array

    def __lt__(self, other):
        return self.value < other.value

class Solution:

    
    def mergeKArrays(self, arr):
        temp = []
        for i in range(len(arr)):
            temp.append(headElementStruct(arr[i][0],i,0))
        heapq.heapify(temp)

        while temp:
            minElement = heapq.heappop(temp)
            print(minElement.value)
            if minElement.idx_in_array + 1 < len(arr[minElement.array_location]):
                nextElementToGoIn = headElementStruct(
                    arr[minElement.array_location][minElement.idx_in_array+1], minElement.array_location, minElement.idx_in_array+1)
                heapq.heappush(temp, nextElementToGoIn)
        
sln = Solution()
sln.mergeKArrays([[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10]])
