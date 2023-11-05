class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        
        if len(arr) <= k:
            return max(arr)
        
        cur_player = arr[0]
        win_streak = 0
        
        Q = deque(arr[1:])
        
        while win_streak != k:
            opponent = Q.popleft()
            
            if cur_player > opponent:
                Q.append(opponent)
                win_streak += 1
            else:
                Q.append(cur_player)
                cur_player = opponent
                win_streak = 1
        
        return cur_player