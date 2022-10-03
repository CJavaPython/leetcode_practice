"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i=0
        while i < len(s):
            bracket = s[i]
            if bracket in "({[":
                stack.append(bracket)
            else:
                if len(stack)==0:
                    return False
                lbracket = stack.pop()
                if lbracket=="(":
                    if bracket!=")":
                        return False
                elif lbracket=="{":
                    if bracket!="}":
                        return False
                elif lbracket=="[":
                    if bracket!="]":
                        return False
            i+=1
        if len(stack)>0:
            return False
        return True

s = Solution()
print(s.isValid(s = "()")) # True
print(s.isValid(s = "()[]{}")) # True
print(s.isValid(s = "(]")) # False