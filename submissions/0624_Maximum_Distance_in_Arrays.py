class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)
        ss = [(i, arrays[i][0]) for i in range(m)]
        es = [(i, arrays[i][-1]) for i in range(m)]

        ss.sort(key=lambda x:x[1])
        es.sort(key=lambda x:x[1], reverse=True)

        maxDist = 0
        for currId in range(m):
            s = arrays[currId][0]
            e = arrays[currId][-1]

            _sId, _s = ss[0]
            if _sId == currId:
                _sId, _s = ss[1]
            
            _eId, _e = es[0]
            if _eId == currId:
                _eId, _e = es[1]
            
            maxDist = max(maxDist, e - _s, _e - s)

        return maxDist

