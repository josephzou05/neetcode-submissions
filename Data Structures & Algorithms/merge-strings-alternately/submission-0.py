class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) < len(word2):
            length = len(word1)
        else:
            length = len(word2)
        result = ""
        for i in range(length):
            result += word1[i]
            result += word2[i]
        if len(word1) < len(word2):
            result += word2[length:]
        else:
            result += word1[length:]
        return result
