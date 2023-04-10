class Solution:
    def isValid(self, s: str) -> bool:
        # 1. Creating an open to close bracket map.
        # 2. Initialize an empty stack.
        # 3. For every para in s:
        # 4.    # If para == open => stack.push(map[para])
        # 5.    # Else:
        # 6.        If not stack: return False
        # 7.        If stack.pop() != para: return False
        # 8. return not stack
        
        open_to_close = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }
        
        stack = []
        
        for para in s:
            if para in open_to_close:
                stack.append(open_to_close[para])
            elif not stack:
                return False
            elif stack.pop() != para:
                return False
        
        return not stack