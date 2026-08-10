class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = -1
        for i in range(len(arr)-1):
            for j in range(i + 1, len(arr)):
                if arr[j] > max:
                    max = arr[j]
            arr[i] = max
            max = -1
        arr[len(arr)-1] = -1
        return arr        