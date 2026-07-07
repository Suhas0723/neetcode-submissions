class Solution:
    def isValid(self, s: str) -> bool:
        sets = {')': '(', '}': '{', ']': '['}

        stack = []

        for i in s:
            if i in sets.values():
                stack.append(i)
            else:
                if not stack or stack.pop() != sets[i]:
                    return False
                
        return not stack