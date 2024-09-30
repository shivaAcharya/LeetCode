class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = Counter(tasks)
        max_heap = [-cnt for cnt in counter.values()]
        heapq.heapify(max_heap)
        
        Q = deque() # [-cnt, cooldown]
        time = 0
        
        while max_heap or Q:
            
            time += 1
            
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    Q.append((cnt, time + n))
            
            if Q and Q[0][1] == time:
                heapq.heappush(max_heap, Q.popleft()[0])
        
        return time
                               
    """
    
    max_heap = [-2]
    Q = [(-2, 3), (-1)]
    time = 4
    while 
        cnt = -1
    
    """
        