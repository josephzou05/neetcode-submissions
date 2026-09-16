class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #boyer moore
        element1, element2, count1, count2 = -1, -1, 0, 0

        for num in nums:
            if count1 == 0:
                element1 = num
                count1 += 1
            elif count2 == 0 and num != element1:
                element2 = num
                count2 += 1
            elif num == element1:
                count1 += 1
            elif num == element2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        result = []
        freq1, freq2 = 0, 0
        for num in nums:
            if num == element1:
                freq1 += 1
            if num == element2:
                freq2 += 1
        if freq1 > (len(nums) // 3):
            result.append(element1)
        if freq2 > (len(nums) // 3):
            result.append(element2)
        return result