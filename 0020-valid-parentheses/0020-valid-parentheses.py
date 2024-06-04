class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paras = {'(' : ')', '{' : '}', '[' : ']'}

        for para in s:
            if para in paras:
                stack.append(paras[para])
            elif not stack or para != stack.pop():
                return False

        return not stack
