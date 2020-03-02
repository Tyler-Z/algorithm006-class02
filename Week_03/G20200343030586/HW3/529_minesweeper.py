"""
529. 扫雷游戏
让我们一起来玩扫雷游戏！

给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。

现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板：

如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。
如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的方块都应该被递归地揭露。
如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。
如果在此次点击中，若无更多方块可被揭露，则返回面板。

"""


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r = [1, 1, 0, 0, -1, -1, -1, 1]
        c = [0, 1, 1, -1, 1, 0, -1, -1]

        board1 = [[i for i in board[xx]] for xx in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'M':
                    for k in range(8):
                        if self.isle(len(board), len(board[0]), i + r[k], j + c[k]):
                            if board[i + r[k]][j + c[k]] == 'E':
                                board[i + r[k]][j + c[k]] = '1'
                            elif not board[i + r[k]][j + c[k]] == 'M':
                                board[i + r[k]][j + c[k]] = str(int(board[i + r[k]][j + c[k]]) + 1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = str(board[i][j])
        if not board[click[0]][click[1]] == "E":
            if board[click[0]][click[1]] == 'M':
                board1[click[0]][click[1]] = 'X'
                return board1
            else:
                board1[click[0]][click[1]] = board[click[0]][click[1]]
                return board1
        self.dfs(board, board1, click)
        return board1

    def isle(self, r, l, xx, y) -> bool:
        return r > xx >= 0 and 0 <= y < l

    def dfs(self, board: list, board1: list, click: list):
        r = [1, 1, 0, 0, -1, -1, -1, 1]
        c = [0, 1, 1, -1, 1, 0, -1, -1]
        board1[click[0]][click[1]] = 'B'
        board[click[0]][click[1]] = 'B'
        for i in range(8):
            nr = r[i] + click[0]
            nc = c[i] + click[1]
            if self.isle(len(board), len(board[0]), nr, nc):
                if board[nr][nc] == 'E':
                    click1 = [nr, nc]
                    self.dfs(board, board1, click1)
                elif board1[nr][nc] == 'E':
                    board1[nr][nc] = board[nr][nc]
