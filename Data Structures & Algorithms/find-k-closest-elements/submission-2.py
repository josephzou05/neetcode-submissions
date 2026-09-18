class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        left = beginning
        right = end

        while right - left + 1 is greater than k:
            shrink the boundary 
                increment left or decrement right
            
            if ______ or (______ and ______): <- left is closer
                decrement right
            
            else: <- right is closer
                increment left
        
        return arr[left:right + 1]
        '''

        left = 0
        right = len(arr) - 1

        while (right - left + 1) > k:
            if abs(arr[left] - x) < abs(arr[right] - x) or (abs(arr[left] - x) == abs(arr[right] - x) and arr[left] < arr[right]):
                right -= 1
            else:
                left += 1
        return arr[left:right + 1]