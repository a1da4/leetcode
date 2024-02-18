class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        numUses = [0] * n
        freeRooms = [room for room in range(n)]
        endTimes = []

        for start, end in sorted(meetings):
            while endTimes:
                prevEnd, room = heapq.heappop(endTimes)
                if prevEnd <= start:
                    heapq.heappush(freeRooms, room)
                else:
                    heapq.heappush(endTimes, [prevEnd, room])
                    break
            if freeRooms:
                room = heapq.heappop(freeRooms)
                heapq.heappush(endTimes, [end, room])
            else:
                prevEnd, room = heapq.heappop(endTimes)
                heapq.heappush(endTimes, [end + (prevEnd - start), room])
            numUses[room] += 1

        return numUses.index(max(numUses))
