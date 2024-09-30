class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        ROWS = len(wall)
        hashmap = defaultdict(int)

        for r in range(ROWS):
            gaps = 0
            for c in range(len(wall[r]) - 1):
                gaps += wall[r][c]
                hashmap[gaps] += 1
        max_gaps = max(hashmap.values()) if hashmap else 0
        return ROWS - max_gaps   