class Solution:
    def findOrder(
        self, 
        numCourses: int, 
        prerequisites: List[List[int]],
    ) -> List[int]:
        isFinished = [False for _ in range(numCourses)]
        numRequired = {course: 0 for course in range(numCourses)}
        nextCourses = {course: [] for course in range(numCourses)}
        for course1, course2 in prerequisites:
            numRequired[course1] += 1
            nextCourses[course2].append(course1)

        answer = []
        
        queue = deque(
            [
                course for course in range(numCourses)
                if numRequired[course] == 0
            ]
        )
        while queue:
            course = queue.popleft()
            answer.append(course)
            isFinished[course] = True
            for nextCourse in nextCourses[course]:
                numRequired[nextCourse] -= 1
                if numRequired[nextCourse] == 0:
                    queue.append(nextCourse)

        return answer if sum(isFinished) == numCourses else []
        
