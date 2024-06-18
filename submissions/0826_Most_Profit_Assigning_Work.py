class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        answer = 0
        tasks = [(diff, prof) for diff, prof in zip(difficulty, profit)]
        tasks.sort(key=lambda x:x[1], reverse=True)
        for w in sorted(worker):
            prof = 0
            for task in tasks:
                if task[0] <= w:
                    prof = task[1]
                    break
            answer += prof
        
        return answer
