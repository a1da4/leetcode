class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        answer = []
        m, n = len(mat), len(mat[0])
        rId, cId = 0, 0
        
        def up(rId, cId):
            while 0 <= rId < m and 0 <= cId < n:
                answer.append(mat[rId][cId])
                rId -= 1
                cId += 1
            return rId, cId

        def down(rId, cId):
            while 0 <= rId < m and 0 <= cId < n:
                answer.append(mat[rId][cId])
                rId += 1
                cId -= 1
            return rId, cId
        
        while len(answer) < m * n:
            rId, cId = up(rId, cId)
            rId += 1
            cId -= 1
            if cId == n - 1:
                rId += 1
            else:
                cId += 1
            
            rId, cId = down(rId, cId)
            rId -= 1
            cId += 1
            if rId == m - 1:
                cId += 1
            else:
                rId += 1

        return answer
