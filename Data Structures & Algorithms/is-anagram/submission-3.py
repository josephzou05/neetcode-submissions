class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        dictt = {}
        for ch in s:
            if ch not in dicts:
                dicts[ch] = 1
            else:
                dicts[ch] += 1
        for ch in t:
            if ch not in dictt:
                dictt[ch] = 1
            else:
                dictt[ch] += 1
        return dicts == dictt        