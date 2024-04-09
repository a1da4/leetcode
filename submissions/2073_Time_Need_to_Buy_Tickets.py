class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        curr = 0
        while tickets[k] > 0:
            for person in range(len(tickets)):
                if tickets[person] == 0:
                    continue
                else:
                    tickets[person] -= 1
                    curr += 1
                if tickets[k] == 0:
                    break
        return curr
