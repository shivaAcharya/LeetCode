class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        """
        
        ptr1, ptr2
        
        cons_win, prev_win
        """
        if k >= len(arr):
            return max(arr)
        
        ptr1, ptr2, cons_win, prev_win = 0, 1, 0, None
        
        while cons_win != k:
            
            if arr[ptr1] > arr[ptr2]:
                arr.append(arr[ptr2])
                if prev_win == arr[ptr1]:
                    cons_win += 1
                else:
                    cons_win = 1
                prev_win = arr[ptr1]
                ptr2 = max(ptr1, ptr2) + 1
            
            else:
                arr.append(arr[ptr1])
                if prev_win == arr[ptr2]:
                    cons_win += 1
                else:
                    cons_win = 1
                
                prev_win = arr[ptr2]
                ptr1 = max(ptr1, ptr2) + 1
        
        return prev_win
    
        """
        [2, 1, 3, 5, 4, 6, 7, 1
        
        
        ptr1 = 2
        ptr2 = 1
        cons_win = 1
        prev_win = None
        
        
        """
                