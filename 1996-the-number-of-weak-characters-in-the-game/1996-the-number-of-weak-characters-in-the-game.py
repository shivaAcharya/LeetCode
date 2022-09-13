class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # Sort in ascending order of attack
        # If attack is same sort in descending order of defense
        
        properties.sort(key=lambda x : (x[0], -x[1]))
        
        weak = 0
        max_defense = 0
        
        for attack, defense in reversed(properties):
            
            if defense < max_defense:
                weak += 1
            
            max_defense = max(max_defense, defense)
        
        return weak