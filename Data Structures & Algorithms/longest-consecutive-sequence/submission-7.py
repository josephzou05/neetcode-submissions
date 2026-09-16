class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numList = set(nums)
        if nums == []:
            return 0
        longest = 1
        for num in numList:
            if (num - 1) not in numList:
                currentLength = 1
                i = 1
                while num + i in numList:
                    currentLength += 1
                    longest = max(longest, currentLength)
                    i += 1
        return longest





#2, 3, 4, 5, 10, 20