class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.sub(r"/+", "/", path)
        print(path.split("/"))

        currDir = []
        for tarDir in path.split("/")[1:]:
            print(f" - tarDir: {tarDir}")
            if currDir == [] and tarDir == "..":
                continue
            elif tarDir == "":
                continue
            elif tarDir == ".":
                continue
            elif tarDir == "..":
                currDir.pop()
            else:
                currDir.append(tarDir)
        
        return "/"+"/".join(currDir)
