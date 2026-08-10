class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        indexS = 0
        for indexT, ch in enumerate(t):
            if indexS < len(s):
                if s[indexS] == t[indexT]:
                    indexS += 1
        return (indexS == len(s))
    
        