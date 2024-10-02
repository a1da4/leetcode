class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        answer = [-1] * len(arr)
        prev = - float("inf")
        rank = 0
        for num, numId in sorted([(num, numId) for numId, num in enumerate(arr)], key=lambda x:x[0]):
            if prev < num:
                rank += 1
            answer[numId] = rank
            prev = num
        
        return answer

