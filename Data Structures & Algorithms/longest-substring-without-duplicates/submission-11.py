class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #1) look at the current window and track each character's latest position
        #2) extend the window. skip duplicates, then move "left" pointer
        lastSeen = {}
        longest = 0
        left = 0

        for right, char in enumerate(s):
            if char in lastSeen and lastSeen[char] >= left:
                left = lastSeen[char] + 1
            
            lastSeen[char] = right
            window = right - left + 1
            longest = max(longest, window)
        return longest


        
            
                                        