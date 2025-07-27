class Solution:
    def minMutation(
        self, 
        startGene: str,
        endGene: str,
        bank: List[str],
    ) -> int:
        if not bank:
            return -1

        if startGene not in bank:
            bank.append(startGene)

        def verify(gene_i: str, gene_j: str) -> bool:
            num_diff = 0
            for ch_i, ch_j in zip(gene_i, gene_j):
                if ch_i != ch_j:
                    num_diff += 1
                    if num_diff > 1:
                        return False

            return True

        graph = defaultdict(list)
        N = len(bank)
        for i in range(N):
            for j in range(i + 1, N):
                gene_i, gene_j = bank[i], bank[j]
                if gene_i == gene_j: continue
                if verify(gene_i, gene_j):
                    graph[gene_i].append(gene_j)
                    graph[gene_j].append(gene_i)

        answer = 0
        visited = set()
        queue = deque([startGene])
        while queue:
            L = len(queue)
            for _ in range(L):
                gene = queue.popleft()
                if gene == endGene:
                    return answer
                visited.add(gene)
                for nextGene in graph[gene]:
                    if nextGene in visited:
                        continue
                    queue.append(nextGene)
            
            answer += 1

        return -1
