class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c2i = {}
        currId = 0
        answer = []

        for currS in strs:
            c = "".join(sorted(currS))
            if c in c2i:
                answer[c2i[c]].append(currS)
            else:
                c2i[c] = currId
                currId += 1
                answer.append([currS])

        return answer
