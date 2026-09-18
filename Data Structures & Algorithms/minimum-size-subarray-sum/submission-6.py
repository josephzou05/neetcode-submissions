class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        subArraySum = 0
        minLen = float("inf")

        for right in range(len(nums)):
            subArraySum += nums[right]

            while subArraySum >= target:
                minLen = min(minLen, right - left + 1)
                subArraySum -= nums[left]
                left += 1

        if minLen == float("inf"):
            return 0

        return minLen


