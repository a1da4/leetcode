class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        currElements = set(mat[0])
        for arr in mat:
            currElements = currElements & set(arr)
        
        if currElements:
            return min(currElements)
        else:
            return -1

