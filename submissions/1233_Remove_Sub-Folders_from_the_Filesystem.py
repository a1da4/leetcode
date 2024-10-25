class Solution:

    class Trie:
        def __init__(self):
            self.is_end = False
            self.children = {}

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = self.Trie()
        answer = []
        folder.sort()
        for path in folder:
            curr = root
            dirs = path.split("/")[1:]
            need_to_add = True
            for i, d in enumerate(dirs):
                if d not in curr.children:
                    curr.children[d] = self.Trie()
                    curr.children[d].is_end = i == (len(dirs) - 1)
                curr = curr.children[d]
                if curr.is_end and i < len(dirs) - 1:
                    need_to_add = False
            if need_to_add:
                answer.append(path)

        return answer
