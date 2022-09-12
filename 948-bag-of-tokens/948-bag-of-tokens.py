class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        
        l, r = 0, len(tokens) - 1
        score = 0
        
        while l <= r:
            
            # Use power if we have enough power
            if tokens[l] <= power:
                power -= tokens[l]
                score += 1
                l += 1
            
            # Consume power
            else:
                if score and l != r:
                    power += tokens[r]
                    score -= 1
                r -= 1
        
        return score