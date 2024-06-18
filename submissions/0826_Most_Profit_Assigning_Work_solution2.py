class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        answer = 0
        taskId = 0
        tasks = [(diff, prof) for diff, prof in zip(difficulty, profit)]
        tasks.sort(key=lambda x:x[1], reverse=True)
        for w in sorted(worker, reverse=True):
            prof = 0
            while taskId < len(tasks):
                if tasks[taskId][0] <= w:
                    prof = tasks[taskId][1]
                    break
                else:
                    taskId += 1 
            answer += prof
        
        return answer

