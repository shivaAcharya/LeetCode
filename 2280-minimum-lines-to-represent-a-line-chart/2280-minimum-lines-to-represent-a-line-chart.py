class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) == 1:
            return 0
        stockPrices.sort()
        lines = 1
        
        for i in range(2, len(stockPrices)):
            y0, y1, y2 = stockPrices[i-2][1], stockPrices[i-1][1], stockPrices[i][1]
            x0, x1, x2 = stockPrices[i-2][0], stockPrices[i-1][0], stockPrices[i][0]
            if (y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0):
                lines += 1
        
        return lines