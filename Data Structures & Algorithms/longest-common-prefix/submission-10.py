class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = ""
        firstWord = strs[0]
        for i in range(len(firstWord)):
            
            for s in strs:
                if i >= len(s):
                    return longestPrefix
                if s[i] != firstWord[i]:
                    return longestPrefix
            longestPrefix += firstWord[i]
        return longestPrefix

                # compare s[i] to strs[0][i]