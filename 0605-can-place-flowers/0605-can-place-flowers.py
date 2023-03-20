class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        count = 0
        L = len(flowerbed)
        for i, plot in enumerate(flowerbed):
            if plot == 0: # If empty
                # If left most, check right
                if i == 0 and i + 1 < L and flowerbed[i + 1] == 0:
                    count += 1
                    flowerbed[i] = 1
                # If right most, check left
                elif i == L - 1 and flowerbed[i-1] == 0:
                    count += 1
                    flowerbed[i] = 1
                # If middle, check left and right
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    count += 1
                    flowerbed[i] = 1
        return count >= n