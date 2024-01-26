"""
s = "2[abc]3[cd]ef"
abcabccdcdef

s = "3[a2[c]]" = 3[acc] = accaccacc

stack = [3, acc]

stack = [abcabc, cdcdcd, ef]

Initialize stack, num, chars
Iterate over s
    If c is digit: add it to num
    if c is alpah: add it to chars
    If c = [: add num to add, set num to 0
    If c == ]: pop num, multiply it to chars and add it to the stack, set chars to ""
    
Return "".join(stack)

s = "3[a]2[bc]"

num = 
chars = a
stack = [aaa, 

"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack, num, chars = [], 0, ""
        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c.isalpha():
                chars += c
            elif c == '[':
                stack.append(chars)
                stack.append(num)
                chars = ""
                num = 0
            else:
                n = stack.pop()
                prev_chars = stack.pop()
                chars = prev_chars + n * chars
        
        return chars
"""
s = "3[a2[c]]"

stack = [
num = 0
chars = ""

"""