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
sln.findCheapestPrice(3,[[0, 1, 100], [1, 2, 100], [0, 2, 500]],0,2,0)
