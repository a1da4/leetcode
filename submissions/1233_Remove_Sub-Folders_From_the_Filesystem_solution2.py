class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        dirs = set()
        answer = []
        for path in sorted(folder):
            curr = ""
            for d in path.split("/")[1:]:
                curr += "/" + d
                if curr in dirs:
                    break
            else:
                answer.append(path)
                dirs.add(path)

        return answer
