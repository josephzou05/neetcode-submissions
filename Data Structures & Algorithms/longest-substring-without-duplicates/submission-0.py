class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        myMap = {}
        longest = 0
        
        left = 0
        for right in range(len(string)):
            if string[right] in myMap:
                left = max(myMap[string[right]] + 1, left)
            myMap[string[right]] = right
            longest = max(longest, right - left + 1)
        return longest


