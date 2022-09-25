class Solution:
    def pathSum(self, nums: List[int]) -> int:
        
        node_val = {num // 10 : num % 10 for num in nums}
        
        Q = deque([(nums[0] // 10, nums[0] % 10)]) # {(11, 3)}
        res = 0
        
        while Q:
            
            #print(Q)
            
            node, cur_sum = Q.popleft()
            level, pos = node // 10, node % 10
            
            node_left = (level + 1) * 10 + 2 * pos - 1
            node_right = (level + 1) * 10 + 2 * pos
            
            
            # If leaf node, add it to res
            if node_left not in node_val and node_right not in node_val:
                res += cur_sum
                
            if node_left in node_val:
                Q.append((node_left, cur_sum + node_val[node_left]))
            
            if node_right in node_val:
                Q.append((node_right, cur_sum + node_val[node_right]))
                
        return res