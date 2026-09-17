class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_dict = defaultdict(int)
        for i, num in enumerate(nums):
            if num in my_dict:
                if abs(my_dict[num] - i) <= k:
                    return True
            my_dict[num] = i
        return False
