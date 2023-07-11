from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row2freq = Counter()
        column2freq = Counter()
        answer = 0
        G = len(grid)
        for i in range(G):
            row = grid[i]
            column = [grid[j][i] for j in range(G)]
            row2freq[str(row)] += 1
            column2freq[str(column)] += 1
        
        columnKeyVocab = set(column2freq.keys())
        for rowKey in row2freq.keys():
            if rowKey in columnKeyVocab:
                answer += row2freq[rowKey] * column2freq[rowKey]
        return answer
