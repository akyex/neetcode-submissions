class Solution:
    def isValid(self, s: str) -> bool:
        valid_stack = []
        connected_dict = {')':'(', ']':'[', '}':'{'}
        if len(s) % 2 != 0:
            return False
        else:
            for char in s:
                if char in connected_dict:
                    if valid_stack and valid_stack[-1] == connected_dict[char]:
                        valid_stack.pop()
                    else:
                        return False
                else:
                    valid_stack.append(char)
            return True if not valid_stack else False
