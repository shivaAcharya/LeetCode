class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        indegrees = defaultdict(int)
        for winner, loser in matches:
            indegrees[loser] += 1
            indegrees[winner] += 0
        
        not_lost = []       
        lost_one = []
        
        for player, lost_times in indegrees.items():
            if lost_times == 1:
                lost_one.append(player)
            if lost_times == 0:
                not_lost.append(player)
        
        not_lost.sort()
        lost_one.sort()
        return [not_lost, lost_one]
        