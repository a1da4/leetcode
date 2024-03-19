class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task2freq = Counter(tasks)
        maxFreq = max(task2freq.values())
        maxCount = 0

        for freq in task2freq.values():
            if freq == maxFreq:
                maxCount+=1

        maxTurns = (maxFreq - 1) * (n + 1) + maxCount
        
        return max(len(tasks), maxTurns)
