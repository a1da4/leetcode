class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        jumps = []
        for i, (nextHeight, currHeight) in enumerate(zip(heights[1    :], heights[:-1])):
            diff = nextHeight - currHeight
            if diff <= 0:
                continue
            heapq.heappush(jumps, diff)
            
            if len(jumps) > ladders:
                bricks -= heapq.heappop(jumps)
            if bricks < 0:
                return i

        return len(heights) - 1
