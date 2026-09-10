class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""
        strs.sort()
        for i in range(len(strs[0])):
            for s in strs:
                if s[i] == strs[0][i]:
                    continue
                else:
                    return commonPrefix
            commonPrefix += strs[0][i]
        return commonPrefix