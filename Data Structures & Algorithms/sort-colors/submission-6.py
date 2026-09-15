class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        i = 0

        while i <= right:
            if nums[i] == 0:
                #swap i, left
                temp = nums[i]
                nums[i] = nums[left]
                nums[left] = temp

                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                #swap i, right
                temp = nums[i]
                nums[i] = nums[right]
                nums[right] = temp

                right -= 1
                #i += 1
        return nums



#[1,0,1,2,1,0,1,2]
# l             r