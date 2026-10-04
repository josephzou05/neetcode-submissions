class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        # Build adjacency list: node -> [(neighbor, travel_time)]
        for source, dest, time in times:
            graph[source].append((dest, time))

        # (total_time_from_start, node)
        minHeap = [(0, k)]
        visited = set()
        maxTime = 0

        while minHeap:
            currTime, node = heapq.heappop(minHeap)

            # First time we pop a node is its shortest possible time
            if node in visited:
                continue

            visited.add(node)
            maxTime = currTime

            # Try traveling to each unvisited neighbor
            for neighbor, travelTime in graph[node]:
                if neighbor not in visited:
                    newTime = currTime + travelTime
                    heapq.heappush(minHeap, (newTime, neighbor))

        return maxTime if len(visited) == n else -1