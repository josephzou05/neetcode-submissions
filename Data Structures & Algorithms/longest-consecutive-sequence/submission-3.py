class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)
        for num in numSet:
            if num - 1 not in numSet:
                temp = 0
                while num + temp in numSet:
                    temp += 1
                if temp > longest:
                    longest = temp
        return longest
