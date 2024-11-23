class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

        def move(row: List[str]) -> List[str]:
            N = len(row)
            empId = N - 1
            for i in range(N - 1, -1, -1):
                if row[i] == "#":
                    row[i], row[empId] = row[empId], row[i]
                    empId -= 1
                if row[i] == "*":
                    empId = i - 1
            return row

        m, n = len(box), len(box[0])
        answer = [[""] * m for _ in range(n)]
        for i in range(m):
            row = move(box[i])
            for j in range(n):
                answer[j][m - 1 - i] = row[j]
        return answer

