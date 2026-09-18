class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26

        if len(s1) > len(s2):
            return False

        for c in s1:
            freq1[ord(c) - ord('a')] += 1

        for i in range(0, len(s1)):
            freq2[ord(s2[i]) - ord('a')] += 1
        if freq1 == freq2:
            return True
        
        left = 1
        right = len(s1)
        while right < len(s2):
            freq2[ord(s2[left - 1]) - ord('a')] -= 1
            freq2[ord(s2[right]) - ord('a')] += 1

            if freq1 == freq2:
                return True
            left += 1
            right += 1
        return False