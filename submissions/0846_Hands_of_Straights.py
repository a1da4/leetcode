class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand2freq = Counter(hand)

        min_heap = list(hand2freq.keys())
        heapq.heapify(min_heap)

        while min_heap:
            curr = min_heap[0]
            for i in range(groupSize):
                if hand2freq[curr + i] == 0:
                    return False
                hand2freq[curr + i] -= 1
                if hand2freq[curr + i] == 0:
                    if curr + i != heapq.heappop(min_heap):
                        return False

        return True

