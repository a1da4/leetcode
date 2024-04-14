class Solution:
    def judgeCircle(self, moves: str) -> bool:
        m2f = Counter(moves)
        return m2f["U"] == m2f["D"] and m2f["L"] == m2f["R"]
        
