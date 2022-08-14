class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        
        scores = [0] * len(edges)
        
        for score, node in enumerate(edges):
            scores[node] += score
        
        max_score = max_score_idx = 0
            
        for idx, score in enumerate(scores):   
            if score > max_score:
                max_score = score
                max_score_idx = idx        
        
        
        return max_score_idx