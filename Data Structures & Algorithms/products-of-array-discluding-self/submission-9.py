class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        #result = [1, 1, 1, 1]
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix = result[i] * nums[i]
        #result = [1, 1, 2, 8]
        suffix = 1
        for j in range(len(nums) - 1, -1, -1):
            result[j] = result[j] * suffix
            suffix = suffix * nums[j]

        return result 