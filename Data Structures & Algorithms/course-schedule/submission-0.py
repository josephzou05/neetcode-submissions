class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses
        adjacencyList = [[] for _ in range(numCourses)]

        for source, destination in prerequisites:
            inDegree[destination] += 1
            adjacencyList[source].append(destination)

        queue = deque()

        for course in range(numCourses):
            if inDegree[course] == 0:
                queue.append(course)

        coursesFinished = 0

        while queue:
            course = queue.popleft()
            coursesFinished += 1

            for neighbor in adjacencyList[course]:
                inDegree[neighbor] -= 1

                if inDegree[neighbor] == 0:
                    queue.append(neighbor)

        return coursesFinished == numCourses