class Solution:
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        if not (board or board[0]) and len(word) > 0:
            return False

        self.visited = [[False for j in range(
            len(board[0]))] for i in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j] and not self.visited[i][j]:
                    if self.searchInMatrix(word, i, j, board, self.visited):
                        return True
        return False

    def searchInMatrix(self, word, i, j, board, visited):
        if not word:
            return True

        if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
            return False
        if word[0] == board[i][j] and not visited[i][j]:
            visited[i][j] = True
            if (self.searchInMatrix(word[1:], i, j+1, board, visited) or
                    self.searchInMatrix(word[1:], i+1, j, board, visited) or
                    self.searchInMatrix(word[1:], i, j-1, board, visited) or
                    self.searchInMatrix(word[1:], i - 1, j, board, visited)):
                    return True
            self.visited[i][j] = False
        return False

sln = Solution()
print(sln.exist([
    ["C", "A", "A"],
    ["A", "A", "A"],
    ["B", "C", "D"]],"AAB"))