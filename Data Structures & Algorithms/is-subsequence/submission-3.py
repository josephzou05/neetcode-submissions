class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        indexS = 0
        for index, ch in enumerate(t):
            if indexS < len(s):
                if s[indexS] == t[index]:
                    indexS += 1
        if indexS == len(s):
            return True
        return False
        