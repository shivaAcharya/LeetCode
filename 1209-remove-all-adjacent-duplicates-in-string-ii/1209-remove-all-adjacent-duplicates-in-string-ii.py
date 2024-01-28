class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = [[s[0], 1]] #(c, frq)
        
        for c in s[1:]:              
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
            # print(stack)
        str_builder = []
        for c, frq in stack:
            str_builder.append(c * frq)
        
        return "".join(str_builder)
    