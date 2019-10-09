class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        import heapq
        pq = [(element, 0, idx) for idx, element in enumerate(matrix[0])]
        heapq.heapify(pq)
        result = 0
        while k != 0:
            result, row, col = heapq.heappop(pq)
            if row + 1 < len(matrix):
                heapq.heappush(pq, (matrix[row + 1][col], row + 1, col))
            k -= 1
        return result

    
    # https: // medium.com/brain-framework/kth-smallest-element-in-sorted-matrix-b20400cf878e
    def kthSmallestAlternate(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        import heapq

        pq = [(matrix[0][0], 0, 0)]
        heapq.heapify(pq)
        m = len(matrix)
        n = len(matrix[0])
        visited = set()
        while k > 1:
            top = heapq.heappop(pq)
            row, col = top[1], top[2]
            if row+1 < m and (row+1, col) not in visited:
                heapq.heappush(pq, (matrix[row+1][col], row+1, col))
                visited.add((row+1, col))
            if col+1 < n and (row, col+1) not in visited:
                heapq.heappush(pq, (matrix[row][col+1], row, col+1))
                visited.add((row, col+1))
            k -= 1
        return pq[0][0]

sln = Solution()
sln.kthSmallest(matrix=[
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
], k=8)
