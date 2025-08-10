class Solution:
    def smallestEquivalentString(
        self, 
        s1: str, 
        s2: str, 
        baseStr: str,
    ) -> str:

        parent = [i for i in range(26)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            if px < py:
                parent[py] = px
            else:
                parent[px] = py

        ordA = ord('a')
        for ch1, ch2 in zip(s1, s2):
            union(ord(ch1) - ordA, ord(ch2) - ordA)
        
        answer = ""
        for ch in baseStr:
            answer += chr(find(ord(ch) - ordA) + ordA)
        
        return answer

