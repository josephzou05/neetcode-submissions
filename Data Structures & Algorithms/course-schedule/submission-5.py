class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#1) initialize an array of inDegrees
#2) initialize an adjacency list to keep track of neighbors
#3) add the inDegrees = 0 (basic classes) into a queue
#4) while queue
#   - increment the number of courses finished
#   - decrement the inDegrees of its neighbors
#   - add its neighbors to the queue if their inDegrees are also 0
#5) check if coursesFinished == numCourses
        coursesFinished = 0
        inDegree = [0] * numCourses
        adjacencyList = [[] for i in range(numCourses)]

        for course, prereq in prerequisites:
            inDegree[course] += 1
            adjacencyList[prereq].append(course)
        
        queue = deque()
        for course in range(numCourses):
            if inDegree[course] == 0:
                queue.append(course)
                #keep in mind its integer course
        
        while queue:
            course = queue.popleft()
            coursesFinished += 1
            for neighbor in adjacencyList[course]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        return coursesFinished == numCourses