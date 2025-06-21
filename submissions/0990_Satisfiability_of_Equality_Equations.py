class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = { 
            chr(x): chr(x) 
            for x in range(ord("a"), ord("z") + 1) 
        } 

        def find(x: str) -> str:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: str, b: str) -> None:
            parent[find(a)] = find(b)

        for equation in equations:
            if equation[1]=='=':
                union(equation[0], equation[3])

        for equation in equations:
            if equation[1]=='!':
                if find(equation[0]) == find(equation[3]):
                    return False

        return True
