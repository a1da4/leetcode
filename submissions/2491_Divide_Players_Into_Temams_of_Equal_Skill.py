class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        target = sum(skill) // (len(skill) // 2)
        print(target)

        mod2id = defaultdict(list)
        answer = 0
        matched = 0
        
        for sId, s in enumerate(skill):
            m = (target - s)
            if mod2id[m]:
                answer += s * m
                mod2id[m].pop()
                matched += 2
            else:
                mod2id[s].append(sId)

        if matched < len(skill):
            return -1
        return answer

