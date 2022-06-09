class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        popped_idx = pushed_idx = 0
        stack = []

        while pushed_idx < len(pushed):
            stack.append(pushed[pushed_idx])
            pushed_idx += 1

            while popped_idx < len(popped) and stack and stack[-1] == popped[popped_idx]:
                stack.pop()
                popped_idx += 1

        return not bool(stack)