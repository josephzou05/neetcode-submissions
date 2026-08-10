class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        longest_prefix = ""
        shortest_word = strs[0]
        for i in range(len(shortest_word)):
            curr = strs[0][i]
            for s in strs:
                if s[i] != curr:
                    return longest_prefix
            longest_prefix = longest_prefix + curr
        return longest_prefix
