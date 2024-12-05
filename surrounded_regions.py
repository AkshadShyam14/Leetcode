from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        visited = []

        def bfs(i,j):
            que = deque()
            que.append((i,j))
            while len(que)>0:
                r,s = que.pop()
                visited.append((r,s))
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for i,j in directions:
                    if 0<=r+i<m and 0<=s+j<n and (r+i,s+j) not in visited:
                        if board[r+i][s+j] == 'O':
                            que.append((r+i,s+j)) 

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    if board[i][j] == 'O' and (i,j) not in visited:
                        bfs(i,j)
        
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    board[i][j] = 'X'
        return board
        