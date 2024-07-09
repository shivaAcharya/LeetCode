"""
customers = [[1, 2], [2, 5], [4, 3]]

1 -> 2 t = 3
2 -> 6 t = 8
4 -> 7 t = 11

15 / 3


customers = [[5, 2], [5, 4], [10, 3], [20, 1]]

time = 5 + 2 => 7 + 4 => 11 + 3 => 14
wait = 2 + 2 + 4 + 1 + 3 + 1 => 13 / 4

time = 0
wait += (max(time - arrival, 0) + cook_time)
return wait_time / L


[[2,3],[6,3],[7,5],[11,3],[15,2],[18,1]]
         ^

cur_time = 5
wait_time = 3


"""

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        cur_time = customers[0][0]
        wait_time = 0
        
        for arrival, time in customers:
            cur_time = max(cur_time, arrival)
            wait_time += (cur_time - arrival + time)
            cur_time += time
        
        return wait_time / len(customers)
            