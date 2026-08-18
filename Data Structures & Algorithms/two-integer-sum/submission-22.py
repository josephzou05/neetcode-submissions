class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, num in enumerate(nums):
            my_dict[num] = i
        for i, num in enumerate(nums):
            complement = target - num
            if complement in my_dict and my_dict[complement] != i:
                return [i, my_dict[complement]]
        return []