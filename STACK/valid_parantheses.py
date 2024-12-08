Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true



class Solution:
    def isValid(self, s: str) -> bool:
        list_s = list(s)
        stack = []

        for char in list_s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False
                el = stack.pop()
                if el == "(" and char != ")":
                    return False 
                if el == "[" and char != "]":
                    return False 
                if el == "{" and char != "}":
                    return False 
        if not stack:
            return True
        return False
 
