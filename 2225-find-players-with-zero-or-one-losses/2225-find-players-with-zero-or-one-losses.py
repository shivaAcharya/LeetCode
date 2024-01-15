class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        indegrees = defaultdict(int)
        winners, losers = set(), set()
        for winner, loser in matches:
            winners.add(winner)
            indegrees[loser] += 1
            losers.add(loser)
        
        not_lost = []
        for winner in winners:
            if winner not in losers:
                not_lost.append(winner)
        
        lost_one = []
        for loser, lost_times in indegrees.items():
            if lost_times == 1:
                lost_one.append(loser)
        
        not_lost.sort()
        lost_one.sort()
        return [not_lost, lost_one]
        