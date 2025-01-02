class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a", "e", "i", "o", "u"}
        bools = [word[0] in vowels and word[-1] in vowels for word in words]

        cumNums = []
        cumNum = 0
        for b in bools:
            if b:
                cumNum += 1
            cumNums.append(cumNum)

        answer = []
        for query in queries:
            if query[0] == 0:
                answer.append(cumNums[query[1]])
            else:
                answer.append(cumNums[query[1]] - cumNums[query[0] - 1])
        
        return answer

