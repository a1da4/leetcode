class Solution:
    def lengthAfterTransformations(
        self, 
        s: str, 
        t: int,
    ) -> int:
        ch2freq = {
            chr(chId): 0
            for chId in range(
                ord('a'), ord('z') + 1
            )
        }
        for ch in s:
            ch2freq[ch] += 1
        
        mod = 10 ** 9 + 7

        for _ in range(t):
            _ch2freq = {
                chr(chId): 0
                for chId in range(
                    ord('a'), ord('z') + 1
                )
            }
            for ch, freq in ch2freq.items():
                if freq == 0: continue

                if ch == 'z':
                    _ch2freq['a'] = (
                        _ch2freq['a'] + freq
                    ) % mod

                    _ch2freq['b'] = (
                        _ch2freq['b'] + freq
                    ) % mod
                
                else:
                    _ch = chr(ord(ch) + 1)
                    _ch2freq[_ch] = (
                        _ch2freq[_ch] + freq
                    ) % mod

            ch2freq = _ch2freq

        answer = 0
        for freq in ch2freq.values():
            answer = (
                answer + freq
            ) % mod

        return answer

