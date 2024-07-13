class File:
    def __init__(self, isFile: bool = False):
        self.isFile = isFile
        self.files = {}
        self.content = ''

class FileSystem:

    def __init__(self):
        self.root = File()

    def ls(self, path: str) -> List[str]:
        curr = self.root
        files = []
        if path != '/':
            d = path.split('/')
            for i in range(1, len(d)):
                curr = curr.files[d[i]]
            if curr.isFile:
                files.append(d[-1])
                return files
        files = curr.files.keys()
        return sorted(files)
        
    def mkdir(self, path: str) -> None:
        curr = self.root
        d = path.split('/')
        for i in range(1, len(d)):
            if d[i] not in curr.files:
                curr.files[d[i]] = File()
            curr = curr.files[d[i]] 

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.root
        d = filePath.split('/')
        for i in range(1, len(d) - 1):
            curr = curr.files[d[i]]
        if d[-1] not in curr.files:
            curr.files[d[-1]] = File(isFile=True)
        curr = curr.files[d[-1]]
        curr.content += content

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.root
        d = filePath.split('/')
        for i in range(1, len(d) - 1):
            curr = curr.files[d[i]]
        return curr.files[d[-1]].content


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
