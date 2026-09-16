class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        for key, value in counts.items():
            if value > (len(nums) // 3):
                result.append(key)
        return result