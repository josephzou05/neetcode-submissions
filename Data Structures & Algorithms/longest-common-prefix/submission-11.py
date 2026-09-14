class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firstWord = strs[0]
        for i in range(len(firstWord)):
            for string in strs:
                if i >= len(string) or string[i] != firstWord[i]:
                    return string[:i]
        return firstWord