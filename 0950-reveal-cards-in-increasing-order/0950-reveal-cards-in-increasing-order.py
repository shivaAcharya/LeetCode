"""
deck = [17,13,11,2,3,5,7]

deck = [2, 3, 5, 7, 11, 13, 17] 
=> [2, 17, 3, 13, 5, 11, 7]
[3, 13, 5, 11, 7, 17]
[5, 11, 7, 17, 13]
[7, 17, 13, 11]
"""
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        Q = deque([i for i in range(N)])
        deck.sort()
        res = [0] * N
        
        for card in deck:
            # Reveal card
            res[Q.popleft()] = card
            
            if Q:
                Q.append(Q.popleft())
            
        return res
    