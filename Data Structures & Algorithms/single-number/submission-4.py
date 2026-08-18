class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_set = set()
        for num in nums:
            if num not in my_set:
                my_set.add(num)
            else:
                my_set.remove(num)
        return list(my_set)[0]