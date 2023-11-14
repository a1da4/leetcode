class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course2prerequisite = {course: [] for course in range(numCourses)}
        indegrees = [0] * numCourses
        for pair in prerequisites:
            course, prerequisite = pair
            course2prerequisite[course].append(prerequisite)
            indegrees[prerequisite] += 1

        independentCourses = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                independentCourses.append(course)
        
        answer = []
        while independentCourses:
            course = independentCourses.popleft()
            answer.append(course)
            for next_course in course2prerequisite[course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    independentCourses.append(next_course)
        
        if len(answer) == numCourses:
            return answer[::-1]
        else:
            return []
