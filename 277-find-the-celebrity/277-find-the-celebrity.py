# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        poss_cand = 0
        
        for i in range(1, n):
            if knows(poss_cand, i):
                poss_cand = i
        
        # Check if poss_cand is actual candidate:
        for i in range(n):
            if i != poss_cand:
                if not knows(i, poss_cand) or knows(poss_cand, i):
                    return -1
        
        return poss_cand
        

        