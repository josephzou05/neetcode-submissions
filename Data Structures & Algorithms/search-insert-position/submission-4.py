class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2
           #2 = 0 + (5 - 0) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] == target:
                return m
            else:
                l = m + 1
        return l
        #l = 3, r = 5
