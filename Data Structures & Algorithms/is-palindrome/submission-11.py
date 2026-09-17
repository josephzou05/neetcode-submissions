class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        reverse = ""
        clean = ""
        stack = []
        for c in s:
            if c.isalnum():
                c = c.lower()
                clean += c
                stack.append(c)
        while stack:
            reverse += stack.pop()
        return clean == reverse

