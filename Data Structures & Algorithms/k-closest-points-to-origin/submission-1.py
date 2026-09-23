class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

#1) create a max heap of size k
#2) for each new element, insert to the max heap
#   - if number of elements is greater than k:
#       - remove element with the max distance

        heap = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = -(x ** 2 + y ** 2)
            heapq.heappush(heap, [distance, x, y])
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        while heap:
            distance, x, y = heapq.heappop(heap)
            result.append([x, y])
        return result



