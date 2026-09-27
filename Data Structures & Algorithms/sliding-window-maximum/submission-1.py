class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque() #index
        left = 0
        right = 0

        while right < len(nums):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            if left > q[0]: #sliding window moved past largest element and it expired
                q.popleft()
                
            if (right + 1) >= k:
                result.append(nums[q[0]])
                left += 1
            right += 1

        return result