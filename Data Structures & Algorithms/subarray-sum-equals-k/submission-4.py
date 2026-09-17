class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        currentSum = 0
        prefixSums = {0 : 1}

        for num in nums:
            currentSum += num
            diff = currentSum - k

            result += prefixSums.get(diff, 0)
            prefixSums[currentSum] = prefixSums.get(currentSum, 0) + 1

        return result

#nums:       [4, -4, 1, 5, 1, 2, -3] k = 3
#prefixSum:  [4,  0, 1, 6, 7, 9,  6]