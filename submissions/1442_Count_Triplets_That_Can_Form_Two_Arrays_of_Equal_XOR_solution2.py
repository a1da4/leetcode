class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        answer = 0
        N = len(arr)

        xor2freq = defaultdict(int)
        xor2freq[0] = 1
        xor2total = defaultdict(int)

        currXor = 0
        for currId in range(N):
            currXor ^= arr[currId]
            answer += xor2freq[currXor] * currId - xor2total[currXor]
            xor2total[currXor] += currId + 1
            xor2freq[currXor] += 1

        return answer

