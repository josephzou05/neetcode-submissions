class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        indexOfS = 0
        indexOfT = 0

        while indexOfS < len(s) and indexOfT < len(t):
            if s[indexOfS] == t[indexOfT]:
                indexOfS += 1
                indexOfT += 1
            else:
                indexOfS += 1
        return len(t) - indexOfT