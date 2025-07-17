class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        nums = [num % k for num in nums]
        num2ids = defaultdict(list)
        for i, num in enumerate(nums):
            num2ids[num].append(i)

        def countAB(a: int, b: int) -> int:
            count = 0
            A, B = num2ids[a], num2ids[b]
            Na, Nb = len(A), len(B)
            aId, bId, count, turn = 0, 0, 0, 0
            while True:
                if turn == 0:
                    while bId < Nb and (aId > 0 and B[bId] <= A[aId - 1]):
                        bId += 1
                    if bId == Nb: break
                    count += 1
                    turn = 1
                    _bId = B[bId]
                    while aId < Na and A[aId] <= _bId:
                        aId += 1
                else:
                    while aId < Na and (bId > 0 and A[aId] <= B[bId - 1]):
                        aId += 1
                    if aId == Na: break
                    count += 1
                    turn = 0
                    _aId = A[aId]
                    while bId < Nb and B[bId] <= _aId:
                        bId += 1

            return count
        
        answer = 0
        for a in range(k):
            for b in range(k):
                if len(num2ids[a]) + len(num2ids[b]) < answer:
                    continue
                answer = max(
                    answer,
                    countAB(a, b),
                )

        return answer

