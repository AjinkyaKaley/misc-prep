class Solution(object):
    def numDistinctIslands(self, grid):
        seen = set()

        def explore(r, c, di=0):
            if (0 <= r < len(grid) and 0 <= c < len(grid[0]) and
                    grid[r][c] and (r, c) not in seen):
                seen.add((r, c))
                shape.append(di)
                explore(r+1, c, 1)
                explore(r-1, c, 2)
                explore(r, c+1, 3)
                explore(r, c-1, 4)
                shape.append(0)

        shapes = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                shape = []
                explore(r, c)
                if shape:
                    shapes.add(tuple(shape))

        return len(shapes)

sln = Solution()
sln.numDistinctIslands([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [
                       0, 0, 0, 1, 1], [0, 0, 0, 1, 1]])
