class TrieNode:
    def __init__(self):
        self.links = {}
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.links:
                    node.links[char] = TrieNode()
                node = node.links[char]
            node.end = True
        answer = set()
        initialChars = set(root.links.keys())

        def search(rowId: int, colId: int, node, word: str):
            if rowId < 0 or rowId > len(board) - 1:
                return
            if colId < 0 or colId > len(board[0]) - 1:
                return

            char = board[rowId][colId]
            if char in node.links:
                word += char
                node = node.links[char]
                board[rowId][colId] = "_"
                if node.end and word not in answer:
                    answer.add(word)
                    node.end = False
                search(rowId + 1, colId, node, word)
                search(rowId - 1, colId, node, word)
                search(rowId, colId + 1, node, word)
                search(rowId, colId - 1, node, word)
                board[rowId][colId] = char
        
        for rowId in range(len(board)):
            for colId in range(len(board[0])):
                if board[rowId][colId] in initialChars:
                    search(rowId, colId, root, "")

        return list(answer)
