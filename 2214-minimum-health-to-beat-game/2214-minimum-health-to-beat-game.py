class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        
                
        health = 0
        armor_damage = 0
        
        for dam in damage:
            
            armor_damage = max(armor_damage, dam)            
            health += dam
        
        return health - min(armor, armor_damage) + 1 
        
        '''
        [2, 7, 4, 3]
        armor = 4
        
        
        
        health = 17
        armor_damage = 4
        
        
        '''