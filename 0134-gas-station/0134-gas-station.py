class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # https://leetcode.com/problems/gas-station/solution/
        
        total_tank = cur_tank = 0              
        start_station = 0
               
        for i, fuel in enumerate(gas):
            cur_tank += fuel - cost[i]
            total_tank += fuel - cost[i]
            if cur_tank < 0:
                cur_tank = 0
                start_station = i + 1
        
        return start_station if total_tank >= 0 else -1
        
        ############### BRUTE-FORCE O(N^2) APPROACH ----> TLE ##############
        '''
        Example 1:
        start -> 4
                
        4 => 0 + 5 = 5
        0 => 5 - 2 + 1 = 4
        1 => 4 - 4 + 2 = 2
        2 => 2 - 
        
        possible_start = [4, 5]
        
        Algorithm:
        1. Iterate over gas and cost to find possible circuit.
        2. Create a helper function is_circuit_complete (idx) --> Bool:
        3.  Simulate gas using cost
        4.  Return true if can be returned to idx else False
        5. Short-circuit if returned True
        6. Return -1 after the end of the loop.      
        
        '''
        N = len(gas)
        
        
        def is_crkt_comp(idx):
            
            tank = 0
            for cur_st in range(idx, N + idx):
                cur_st %= N
                tank += (gas[cur_st] - cost[cur_st]) # tank = 0 + 4 - 1 => 3
                if tank < 0: return False
            return True
        
        # Return -1 if sum(gas) < sum(cost)
        if sum(gas) < sum(cost): return -1
        
        for station, fuel in enumerate(gas):
            # If enough fuel found
            if fuel >= cost[station] and is_crkt_comp(station):
                return station
        
        return -1
        
        '''
        DRY RUN:
                  0, 1, 2, 3, 4
        1. gas = [1, 2, 3, 4, 5]
          cost = [3, 4, 5, 1, 2]
          
          is_crkt_comp (3) => ?
            tank = 0, 3, 6, 4, 2
            cur_st => 3 -> 7 || 3, 4, 5, 6, 7
            cur_st = 3, 4, 0, 1, 2
            tank => 2 + 3 -
            
        '''