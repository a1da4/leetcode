class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        numG = len(g)
        numS = len(s)
        answer = 0
        gId = 0
        sId = 0
        while gId < numG and sId < numS:
            if g[gId] <= s[sId]:
                answer += 1
                gId += 1
                sId += 1
            else:
                gId += 1
        return answer
