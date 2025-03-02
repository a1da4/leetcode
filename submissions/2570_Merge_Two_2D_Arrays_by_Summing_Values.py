class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        heap = []
        for item in (nums1 + nums2):
            heapq.heappush(heap, item)
        
        answer = []
        prevId = -1
        prevVal = -1
        while heap:
            item = heapq.heappop(heap)
            if prevId == item[0] and prevId > 0:
                answer.append([prevId, prevVal + item[1]])
                prevId = -1
                prevVal = -1
            else:
                if prevId > 0:
                    answer.append([prevId, prevVal])
                prevId, prevVal = item
        
        if prevId > 0:
            answer.append([prevId, prevVal])

        return answer
