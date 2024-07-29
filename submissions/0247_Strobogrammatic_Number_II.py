class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        validPairs = [['0', '0'], ['1', '1'],
                      ['6', '9'], ['8', '8'],
                      ['9', '6']]
        
        currLen = n % 2
        queue = ['0', '1', '8'] if currLen else ['']
        queue = deque(queue)

        while currLen < n:
            currLen += 2
            N = len(queue)
            for _ in range(N):
                curr = queue.popleft()
                for pair in validPairs:
                    if currLen != n or pair[0] != '0':
                        queue.append(pair[0] + curr + pair[1])
        
        return [num for num in queue]

