class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_hash = {}
        maxCount = 0
        result = 0

        for num in nums:
            my_hash[num] = my_hash.get(num, 0) + 1
            if maxCount < my_hash[num]:
                result = num
                maxCount = my_hash[num]
        return result