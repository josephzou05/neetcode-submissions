class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # keep two pointers: start, end
        # if the sum is greater than target, decrement end pointer
        # if the sum is less than target, increment start pointer
        # else return two pointers
        start = 0
        end = len(numbers) - 1
        while True:
            if numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                return [start + 1, end + 1]
