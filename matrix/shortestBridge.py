class Solution:


    def shortestBridge(self, grid):
        
        m = len(grid)
        n = len(grid[0])
        seen = set()

        def dfs(r, c, component):
            
            if 0 <= r < m and 0 <= c < n and grid[r][c] and (r,c) not in seen:
                component.append((r, c))
                seen.add((r, c))
                dfs(r + 1, c, component)
                dfs(r, c + 1, component)
                dfs(r - 1, c, component)
                dfs(r, c - 1, component)
            return component

        source = None
        dest = None

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and not source:
                    source = dfs(r, c, [])
                elif grid[r][c] == 1 and not dest:
                    dest = dfs(r, c, [])
                    

        import collections
        queue = collections.deque([(*node, 0) for node in source])
        target = set(dest)
        depth = 0
        visited = set(source)
        while queue:
            r, c, depth = queue.popleft()
            if (r, c) in target:
                return depth - 1

            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if (nr, nc) not in visited:
                    if 0 <= nr < m and 0 <= nc < n:
                        queue.append((nr, nc, depth + 1))
                        visited.add((nr, nc))
        
sln = Solution()
sln.shortestBridge([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [
                   1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]])
