class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankVocab = set(bank)
        visited = set()
        visited.add(startGene)
        genes = ["A", "C", "G", "T"]
        queue = deque()
        queue.append(startGene)
        mutations = 0
        while queue:
            numGenes = len(queue)
            for _ in range(numGenes):
                currGene = queue.popleft()
                if currGene == endGene:
                    return mutations
                for gene_id in range(8):
                    for gene in genes:
                        newGene = currGene[:gene_id] + gene + currGene[gene_id+1:]
                        if newGene in bankVocab and newGene not in visited:
                            visited.add(newGene)
                            queue.append(newGene)
            mutations += 1
        return -1
