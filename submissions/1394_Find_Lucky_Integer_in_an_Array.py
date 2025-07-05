class Solution:
    def findLucky(self, arr: List[int]) -> int:
        answer = -1
        for num, freq in Counter(arr).items():
            if num == freq:
                answer = max(answer, num)
            
        return answer
