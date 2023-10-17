class Solution:
    def simplifyPath(self, path: str) -> str:
        currDir = []
        for tarDir in path.split("/")[1:]:
            if tarDir in set(["", "."]):
                continue
            elif tarDir == "..":
                if currDir == []:
                    continue
                currDir.pop()
            else:
                currDir.append(tarDir)
        
        return "/"+"/".join(currDir)
