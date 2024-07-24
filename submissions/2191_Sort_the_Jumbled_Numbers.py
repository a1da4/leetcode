class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def _convert(num: int) -> int:
            queue = deque([ch for ch in str(num)])
            _num = ""
            while queue:
                _num += str(mapping[int(queue.popleft())])
            return int(_num)
        
        _num2num = defaultdict(list)
        _nums = set()
        heap = []
        for num in nums:
            _num = _convert(num)
            _num2num[_num].append(num)
            if _num not in _nums:
                _nums.add(_num)
                heapq.heappush(heap, _num)

        answer = []
        while heap:
            answer += _num2num[heapq.heappop(heap)]
        
        return answer
