class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        dict_ = Counter()
        
        for word in words:
            lst = []
            for letter in word:
                lst.append(morse_code[ord(letter) - ord('a')])
            
            dict_["".join(lst)] += 1
        
        return len(dict_)