class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        freq = [0] * 26
        for c in s1:
            freq[ord(c) - ord('a')] += 1

        freqLong = [0] * 26
        for c in s2[:len(s1)]:
            freqLong[ord(c) - ord('a')] += 1

        if freq == freqLong:
            return True

        l = 0
        r = len(s1)

        while r < len(s2):
            freqLong[ord(s2[l]) - ord('a')] -= 1
            freqLong[ord(s2[r]) - ord('a')] += 1

            if freq == freqLong:
                return True

            l += 1
            r += 1

        return False
