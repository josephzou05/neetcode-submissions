class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1
        print(my_dict)
        currentMax = 0
        currentMaxKey = 0
        for key, value in my_dict.items():
            if value > currentMax:
                currentMax = value
                currentMaxKey = key
        return currentMaxKey
