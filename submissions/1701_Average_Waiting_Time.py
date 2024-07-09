class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waits = []
        curr = 1
        for customer in customers:
            arrive, time = customer
            if arrive > curr:
                curr = arrive
            curr += time
            waits.append(curr - arrive)
        
        return sum(waits) / len(waits)
