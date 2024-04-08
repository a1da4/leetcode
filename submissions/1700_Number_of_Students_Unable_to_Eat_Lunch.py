class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students and sandwiches:
            newStudents = []
            while students and students[0] != sandwiches[0]:
                student = students.pop(0)
                newStudents.append(student)
            if not students:
                return len(newStudents)
            else:
                students.pop(0)
                sandwiches.pop(0)
                students = students + newStudents
        return len(students)
