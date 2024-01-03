class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        currDev = 0
        answer = 0
        for row in bank:
            devices = sum([1 if char == "1" else 0 for char in row])
            if devices == 0:
                continue
            answer += currDev * devices
            currDev = devices
        return answer
