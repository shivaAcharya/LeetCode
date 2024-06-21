class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        # Find initially satisfied customers
        satisfied = sum([c for c, g in zip(customers, grumpy) if not g])
        
        # Use sliding window to find maximum unsatisfied cust that can be satisfied
        l = window = max_window = 0
        for r, grump in enumerate(grumpy):
            if grump:
                window += customers[r]
                
            if r - l  + 1 > minutes:
                if grumpy[l]:
                    window -= customers[l]
                l += 1
            
            max_window = max(max_window, window)
            
        return satisfied + max_window
        