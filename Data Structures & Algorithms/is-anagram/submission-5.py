class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        copy_s = sorted(s)
        copy_t = sorted(t)
        result = True
        if len(copy_s) == len(copy_t):
            for i in range(len(copy_t)):
                if copy_t[i] != copy_s[i]:
                    result = False
        else:
            return False

        return result
        