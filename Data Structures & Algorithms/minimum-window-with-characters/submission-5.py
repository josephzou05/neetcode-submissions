class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # 1) Frequency mapping of t
        countT = {}
        window = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have = 0
        need = len(countT)
        result = [-1, -1]
        resultLen = float("infinity")

        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)
            
            if c in countT and window[c] == countT[c]:
                have += 1 #check against window
            
            while have == need: #found a match! now shrink window
                if (right - left + 1) < resultLen:
                    result = [left, right]
                    resultLen = right - left + 1
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = result
        if resultLen == float("infinity"):
            return ""
        return s[left : right + 1]