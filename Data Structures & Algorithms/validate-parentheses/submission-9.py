class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_check = {')':'(', ']':'[', '}':'{'}

        #if the input is odd, then no possible solution exists
        if len(s) % 2 != 0:
            return False
        else:
            for char in s:
                if char in dict_check:
                    #if stack is not empty and last entry of stack is in dict"
                    if stack and stack[-1] == dict_check[char]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(char)
            return True if not stack else False