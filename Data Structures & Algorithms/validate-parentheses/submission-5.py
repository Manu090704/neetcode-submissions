class Solution:
    def isValid(self, s: str) -> bool:
        open = []
        closeOpen = {"}":"{", "]":"[", ")":"("}
        for char in s:
            if char in closeOpen:
                if open and open[-1] == closeOpen[char]:
                    open.pop()
                else:
                    return False
            else:
                open.append(char)
        return True if not open else False
        