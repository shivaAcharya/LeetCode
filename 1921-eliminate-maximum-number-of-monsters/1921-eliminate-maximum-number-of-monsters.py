class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        time_to_city = [dis / sp for sp, dis in zip(speed, dist)]
        time_to_city.sort()
        # print(time_to_city)
        
        minutes = 0
        
        for mon in time_to_city:
            if mon > minutes:
                # print("Incrementing minutes")
                minutes += 1
            else:
                break
        
        return minutes