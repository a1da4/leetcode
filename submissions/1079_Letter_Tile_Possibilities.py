class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        answer = 0
        N = len(tiles)
        ch2freq = Counter(tiles)

        def count(ch2freq: Dict[str, int]) -> int:
            total = 0
            for ch in ch2freq.keys():
                if ch2freq[ch] == 0:
                    continue
                total += 1
                ch2freq[ch] -= 1
                total += count(ch2freq)
                ch2freq[ch] += 1
            return total

        return count(ch2freq)


