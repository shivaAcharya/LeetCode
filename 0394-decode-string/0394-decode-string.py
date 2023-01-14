class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []; cur_num = 0; cur_str = ""
        
        for c in s:
            if c == '[':
                stack.append(cur_num)
                stack.append(cur_str)
                cur_num = 0; cur_str = ""
            elif c == ']':
                prev_str, num = stack.pop(), stack.pop()
                cur_str = prev_str + num * cur_str
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)
            else:
                cur_str += c
        
        return cur_str
            
            
            
        