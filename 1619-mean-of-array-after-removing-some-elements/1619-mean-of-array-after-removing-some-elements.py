class Solution:
    def trimMean(self, arr: List[int]) -> float:
        trim_idx = len(arr) // 20
        arr.sort()
        
        return (sum(arr[trim_idx:]) - sum(arr[len(arr) - trim_idx:])) / (0.9 * len(arr))