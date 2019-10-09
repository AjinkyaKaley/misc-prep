class Solution:
    def exist(self, board, word: str):
        m = len(board)
        n = len(board[0])

        def search(i, j, word):
            if not word:
                return True

            if 0 <= i < m and 0 <= j < n and board[i][j] != '#':
                if word[0] == board[i][j]:
                    temp = board[i][j]
                    board[i][j] = '#'
                    if search(i + 1, j, word[1:]) or search(i, j + 1, word[1:]) or search(i - 1, j, word[1:]) or search(i, j - 1, word[1:]):
                        return True
                    board[i][j] = temp
            return False

        for i in range(m):
            for j in range(n):
                if search(i, j, word):
                    return True
        return False

sln = Solution()
sln.exist(board=
          [
              ['A', 'B', 'C', 'E'],
              ['S', 'F', 'C', 'S'],
              ['A', 'D', 'E', 'E']
          ], word="ABCCED")
