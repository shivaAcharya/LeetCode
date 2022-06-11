class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dict_ = {}
        max_edges = 0
        
        for row in wall:
            prefix_sum = 0
            for i in range(len(row) - 1):
                prefix_sum += row[i]
                dict_[prefix_sum] = dict_.get(prefix_sum, 0) + 1
                max_edges = max(max_edges, dict_[prefix_sum])
        
        return len(wall) - max_edges
        