class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numList = set(nums)
        if nums == []:
            return 0
        longest = 1
        for num in numList:
            if (num - 1) not in numList:
                currentLength = 1
                while num + currentLength in numList:
                    currentLength += 1
                    longest = max(longest, currentLength)
        return longest





#2, 3, 4, 5, 10, 20