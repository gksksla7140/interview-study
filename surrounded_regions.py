class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        q = collections.deque([])
        for x in range(len(board)):
            for y in range(len(board[0])):
                if y in [0, len(board[0]) -1] or x in [0, len(board) -1] and board[x][y] == 'O':
                    q.append((x,y))
        while q:
            x,y = q.popleft()
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'O':
                board[x][y] = 'C'
                q.append((x,y - 1)); q.append((x,y + 1))
                q.append((x - 1, y)); q.append((x + 1, y))
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'C':
                    board[x][y] = 'O'
