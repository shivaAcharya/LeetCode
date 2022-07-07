class Solution:
    def numIslands(self, region: List[List[str]]) -> int:
        ROWS, COLS = len(region), len(region[0])

        islands = 0
        visited = set()

        def dfs(r, c):
            if (r, c) in visited:
                return

            visited.add((r, c))

            # Explore neighbors
            for row, col in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= row < ROWS and 0 <= col < COLS and region[row][col] == "1":
                    dfs(row, col)


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and region[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands 