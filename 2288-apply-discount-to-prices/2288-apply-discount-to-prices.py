import re
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sentence_list = sentence.split()
        
        for i, word in enumerate(sentence_list):
            if re.match("\$\d+$", word):
                price = float(word[1:])
                sentence_list[i] = '$' + '{:.2f}'.format((round(price - price * discount / 100, 2)))
        
        return " ".join(sentence_list)
                