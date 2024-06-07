class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        dict_set = set(dictionary)
        dictionary.sort(key=lambda x: len(x))
        res = []
        
        # print(dictionary)
        for word in sentence.split():
            for root in dictionary:
                if word.startswith(root):
                    res.append(root)
                    break
            else:
                res.append(word)
        
        return " ".join(res)
        