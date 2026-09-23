class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        my_dict = {}
        result = 0
        for right in range(len(s)):
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]] + 1)
            my_dict[s[right]] = right
            result = max(result, right - left + 1)
        return result


#1) sliding window
#2) left pointer at: max(left, last occurrence of duplicate)
#3) right pointer iterating
#4) keep a length var