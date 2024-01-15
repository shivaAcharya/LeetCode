from sortedcontainers import SortedList
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        indegrees = defaultdict(int)
        for winner, loser in matches:
            indegrees[loser] += 1
            indegrees[winner] += 0
        
        not_lost = SortedList()    
        lost_one = SortedList()
        
        for player, lost_times in indegrees.items():
            if lost_times == 1:
                lost_one.add(player)
            if lost_times == 0:
                not_lost.add(player)

        return [not_lost, lost_one]
        