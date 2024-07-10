class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                depth -= 1
                depth = max(depth, 0)
            else:
                depth += 1

        return depth

