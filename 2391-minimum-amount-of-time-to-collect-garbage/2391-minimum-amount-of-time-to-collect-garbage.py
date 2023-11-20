class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        P = G = M = 0
        
        for gar in reversed(garbage):
            travel_time = travel.pop() if travel else 0
            # Collect garbage
            for gar_type in gar:
                if gar_type == "P":
                    P += 1
                elif gar_type == "G":
                    G += 1
                else:
                    M += 1
                    
            # Add Travel Time
            if P:
                P += travel_time
            if G:
                G += travel_time
            if M:
                M += travel_time
        
        return P + G + M
    