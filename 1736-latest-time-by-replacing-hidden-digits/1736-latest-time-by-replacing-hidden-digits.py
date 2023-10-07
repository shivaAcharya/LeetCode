class Solution:
    def maximumTime(self, time: str) -> str:
        
        time = list(time)
        
        for i, c in enumerate(time):
            if c == '?':
                if i == 0:
                    time[i] = '2' if time[1] in '?0123' else '1'
                elif i == 1:
                    time[i] = '3' if time[0] == '2' else '9'
                elif i == 3:
                    time[i] = '5'
                else:
                    time[i] = '9'
                    
        return "".join(time)