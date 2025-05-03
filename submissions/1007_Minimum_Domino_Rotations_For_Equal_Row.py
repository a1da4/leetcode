class Solution:
    def minDominoRotations(
        self, 
        tops: List[int], 
        bottoms: List[int],
    ) -> int:
        N = len(tops)

        def _calcNum(targetNum: int) -> int:
            return N - max(
                tops.count(targetNum),
                bottoms.count(targetNum),
            )

        currSet = {tops[0], bottoms[0]}
        for i in range(1, N):
            currSet &= {tops[i], bottoms[i]}
        
        targetNums = list(currSet)
        if len(targetNums) == 0:
            return -1
        elif len(targetNums) == 1:
            return _calcNum(targetNums[0])
        else:
            return min(
                _calcNum(targetNums[0]),
                _calcNum(targetNums[1]),
            )

