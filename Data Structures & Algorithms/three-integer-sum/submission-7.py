class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index, a in enumerate(nums):
            if a > 0:
                break

            if index > 0 and a == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else: #threeSum is 0 !
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
