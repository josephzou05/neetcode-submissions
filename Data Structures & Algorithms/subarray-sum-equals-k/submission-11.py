class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currentSum = 0
        prefixSums = {0:1}
        result = 0
        for num in nums:
            currentSum += num
            diff = currentSum - k
            result += prefixSums.get(diff, 0)
            prefixSums[currentSum] = prefixSums.get(currentSum, 0) + 1

        return result

'''
1. Keep a running prefix sum
2. Ask: what previous prefix sum would make the difference equal k?
3. Count how many times we've seen that prefix sum
4. Store the current prefix sum
'''