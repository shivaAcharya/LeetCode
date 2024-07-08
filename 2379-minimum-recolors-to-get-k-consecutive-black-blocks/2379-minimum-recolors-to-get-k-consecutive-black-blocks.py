class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        min_ops = white_count = blocks[:k].count('W')
        left = 0
        
        # Sliding Window
        for color in blocks[k:]:
            if color == 'W':
                white_count += 1
            
            if blocks[left] == 'W':
                white_count -= 1
            
            left += 1
            min_ops = min(min_ops, white_count)
        
        return min_ops        
        