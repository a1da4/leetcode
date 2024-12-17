class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap = [(-ord(ch), freq) for ch, freq in Counter(s).items()]
        heapify(heap)
        result = ""

        while heap:
            _ch_id, count = heappop(heap)
            ch = chr(-_ch_id)
            num = min(count, repeatLimit)
            result += ch * num

            if count > num and heap:
                _next_ch_id, next_count = heappop(heap)
                result += chr(-_next_ch_id)
                if next_count > 1:
                    heappush(heap, (_next_ch_id, next_count - 1))
                heappush(heap, (_ch_id, count - num))

        return result

