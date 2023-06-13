# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []
        for i in s:
            if i in ("(", "{", "["):
                stack.append(i)
            elif i in (")", "}", "]") and len(stack) == 0:
                return False
            elif (stack[-1] == '(' and i == ')' or stack[-1] == '[' and i == ']' or stack[-1] == '{' and i == '}'):
                    stack.pop()
            else:
                return False

        return True if (len(stack) == 0) else False


obj = Solution()
print(obj.isValid("{}([)]"))
print(obj.isValid("]"))
print(obj.isValid("()"))
print(obj.isValid("(])"))
