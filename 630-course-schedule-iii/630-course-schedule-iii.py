class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        currentTotalTime = 0
        courses.sort(key=lambda x : x[1])
        for duration, lastDay in courses:
            # Add course
            if currentTotalTime + duration <= lastDay:
                heapq.heappush(heap, -duration)
                currentTotalTime += duration
            elif heap and abs(heap[0]) > duration:
                currentTotalTime += heapq.heappop(heap)
                currentTotalTime += duration
                heapq.heappush(heap, -duration)
            
        
        return len(heap)