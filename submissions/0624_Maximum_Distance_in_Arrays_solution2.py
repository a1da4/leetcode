class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        s = arrays[0][0]
        e = arrays[0][-1]
        maxDist = 0
        for array in arrays[1:]:
            _s = array[0]
            _e = array[-1]
            
            maxDist = max(maxDist, e - _s, _e - s)

            s = min(s, _s)
            e = max(e, _e)

        return maxDist

