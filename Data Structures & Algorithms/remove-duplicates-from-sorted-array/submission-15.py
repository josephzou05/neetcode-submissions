class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nextUniqueIndex = 1
        i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                nums[nextUniqueIndex] = nums[i]
                nextUniqueIndex += 1
            i += 1
        return nextUniqueIndex