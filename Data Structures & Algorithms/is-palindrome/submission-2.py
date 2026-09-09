class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()

        length = len(newStr)
        for i in range(length // 2):
            if newStr[i] != newStr[length - i - 1]:
                return False
        return True


# r a c e c a r