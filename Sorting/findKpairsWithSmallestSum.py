import heapq
class Solution:

    def kSmallestPairs(self, nums1, nums2, k):
        pq = []
        for i in range(len(nums1)):
            pq.append((nums1[i], 1))

        for i in range(len(nums2)):
            pq.append((nums2[i], 2))
        
        heapq.heapify(pq)

        for i in range(k):
            value1, arrId1 = heapq.heappop(pq)

            while heapq:
                value2, arrId2 = heapq.heappop(pq)
                if arrId2 != arrId1:
                    break

            print(str(value1) + "," + str(value2))
            if value1 <= value2:
                heapq.heappush(pq, (value1, arrId1))
            else:
                heapq.heappush(pq, (value2, arrId2))

#    2   4   6
#   +------------
# 1 |  3   5   7
# 7 |  9  11  13
#11 | 13  15  17

    def kSmallestPairsFaster(self, nums1, nums2, k):
        queue = []

        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs
sln = Solution()
print(sln.kSmallestPairsFaster([1, 7, 11], [2, 4, 6], 5))
# sln.kSmallestPairsFaster([1, 1, 2], [1, 2, 3], 2)
