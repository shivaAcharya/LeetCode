# ref: https://leetcode.com/problems/search-suggestions-system/discuss/436674/C++JavaPython-Sort-and-Binary-Search-the-Prefix
# approach 1: sort then binary search
# 1. sort input array
# 2. use binary search to find first index
# 3. check the following 3 words
# time: O(nlogn) ---> python timsort
# space: O(n) ---> might need to scan the entire input array

class Solution:
    
    def __init__(self):
        self.lo = 0
        
        
    def suggestedProducts(self, products, searchWord):
        products.sort() # time O(nlogn)
        array_len = len(products)
        ans = []
        input_char = ""
        

        for chr in searchWord:
            tmp = []
            input_char += chr
            self.binary_search(products, input_char) # find where input_char can be inserted in-order in the products array
            for word_ind in range(self.lo, min(array_len, self.lo + 3)): # check the following 3 words, if valid
                if products[word_ind].startswith(input_char):
                    tmp.append(products[word_ind])
            ans.append(tmp)
        return ans

    def binary_search(self, array, target): # bisect.bisect_left implementation
        hi = len(array)
        lo = self.lo
        while lo < hi:
            mid = (lo + hi) //2
            if array[mid] < target: lo = mid + 1
            else: hi = mid
        self.lo = lo
        return lo