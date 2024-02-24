class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        answer = set([0, firstPerson])

        time2meetings = defaultdict(list)
        for meeting in meetings:
            time2meetings[meeting[2]].append(meeting)

        for time in sorted(time2meetings.keys()):
            currMeetings = time2meetings[time]
            x2y = defaultdict(list)
            for meeting in currMeetings:
                x, y, time = meeting
                x2y[x].append(y)
                x2y[y].append(x)
            currAns = deque(list(answer))
            while currAns:
                currAnswer = currAns.popleft()
                for y in x2y[currAnswer]:
                    if y in answer:
                        continue
                    else:
                        answer.add(y)
                        currAns.append(y)
                        if len(answer) == n:
                            return list(answer)

        return list(answer)
