class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, K: int):
        import heapq
        self.graph = {i: [] for i in range(n+1)}
        for u, v, w in flights:
            self.graph[u] += [(v, w)]
        queue = [(0, src, -1)]

        while queue:
            cost, node, _k = heapq.heappop(queue)
            if node == dst:
                return cost
            if _k < K:
                for v, w in self.graph[node]:
                    heapq.heappush(queue, (cost+w, v, _k+1))

        return -1

sln = Solution()
print(sln.findCheapestPrice(5,
                      [[1, 2, 10], [2, 0, 7], [1, 3, 8], [4, 0, 10], [
                          3, 4, 2], [4, 2, 10], [0, 3, 3], [3, 1, 6], [2, 4, 5]],
                      0,
                      4,
                      1))
