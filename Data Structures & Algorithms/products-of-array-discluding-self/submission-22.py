class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [0] * len(nums)
        #left
        products[0] = 1
        for i in range(1, len(nums)):
            products[i] = nums[i - 1] * products[i - 1]

        #right
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            products[i] = right * products[i]
            right = right * nums[i]
        #print("Left products:", products)
        return products


sol = Solution()
sol.productExceptSelf([-1, 0, 1, 2, 3])
#[1, 2, 4, 6]

#[1, 1, 2, 8]
#[48, 24, 6, 1]

#[-1, 0, 1, 2, 3]

#[1, -1, 0, 0, 0] left
#[0, 6, 6, 3, 1] right