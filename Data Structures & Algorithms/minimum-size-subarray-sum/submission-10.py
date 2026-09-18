class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currentSum = 0
        minLen = float('inf')

        for right in range(len(nums)):
            currentSum += nums[right]
            while currentSum >= target:
                minLen = min(minLen, right - left + 1)
                currentSum -= nums[left]
                left += 1
            #currentSum += nums[right]
        if minLen == float('inf'):
            return 0
        return minLen
