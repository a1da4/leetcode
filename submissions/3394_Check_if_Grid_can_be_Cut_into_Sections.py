class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        def verify(axis: int) -> bool:
            numGap = 0
            rectangles.sort(key=lambda rectangle: rectangle[axis])
            end = rectangles[0][axis + 2]

            for i in range(1, len(rectangles)):
                rectangle = rectangles[i]
                if end <= rectangle[axis]:
                    numGap += 1
                end = max(end, rectangle[axis + 2])

            return numGap > 1
        
        return verify(0) or verify(1)

