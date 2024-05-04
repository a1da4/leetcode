class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        leftId, rightId = 0, len(people) - 1
        answer = 0

        while leftId <= rightId:
            answer += 1
            if people[leftId] + people[rightId] <= limit:
                leftId += 1
            rightId -= 1

        return answer
