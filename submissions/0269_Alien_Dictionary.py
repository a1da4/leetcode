class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjs = defaultdict(set)
        inDegree = Counter({ch: 0 for word in words for ch in word})

        for word_i, word_j in zip(words[:-1], words[1:]):
            for ch_i, ch_j in zip(word_i, word_j):
                if ch_i != ch_j:
                    if ch_j not in adjs[ch_i]:
                        adjs[ch_i].add(ch_j)
                        inDegree[ch_j] += 1
                    break
            else:
                if len(word_j) < len(word_i):
                    return ''
        
        output = []
        queue = deque([ch for ch in inDegree if inDegree[ch] == 0])
        while queue:
            ch = queue.popleft()
            output.append(ch)
            for _ch in adjs[ch]:
                inDegree[_ch] -= 1
                if inDegree[_ch] == 0:
                    queue.append(_ch)

        if len(output) < len(inDegree):
            return ''
        else:
            return ''.join(output)

