class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            if len(trust) == 0:
                return 1
            else:
                return -1
        elif len(trust) == 0:
            return -1
        else:
            judge2freq = Counter([pair[1] for pair in trust])
            trusts = set([pair[0] for pair in trust])
            for judge, freq in judge2freq.items():
                if freq == n - 1 and judge not in trusts:
                    return judge
            return -1
