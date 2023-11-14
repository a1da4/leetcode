class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course2prerequisites = {course:[] for course in range(numCourses)}
        indegree = [0] * numCourses
        finishedCourses = 0

        for pair in prerequisites:
            course, prerequisite = pair
            course2prerequisites[course].append(prerequisite)
            indegree[prerequisite] += 1

        independentCourses = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                independentCourses.append(course)

        while independentCourses:
            course = independentCourses.popleft()
            finishedCourses += 1
            for next_course in course2prerequisites[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    independentCourses.append(next_course)

        return finishedCourses == numCourses
