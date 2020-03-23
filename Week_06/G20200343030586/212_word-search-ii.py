"""
212. 单词搜索 II
给定一个二维网格 board 和一个字典中的单词列表 words，
找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，
其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母在一个单词中不允许被重复使用。

1 把words中的word存入前缀树
2 对board进行深度优先搜索
dfs三个核心部分：
1 新的字符不在搜索范围内，退出
2 新的字符在搜索范围内，且该字符与之前的字符串为words中的一个word, 加入结果集，
并将word结束标志置0，放置重复搜索
3 按深度优先递归搜索
"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i, j, t, s):
            ch = board[i][j]
            if ch not in t:
                return
            t = t[ch]
            if "end" in t and t["end"] == 1:
                res.append(s + ch)
                t["end"] = 0
            board[i][j] = "#"
            if i + 1 < m and board[i + 1][j] != "#":
                dfs(i + 1, j, t, s + ch)
            if i - 1 >= 0 and board[i - 1][j] != "#":
                dfs(i - 1, j, t, s + ch)
            if j + 1 < n and board[i][j + 1] != "#":
                dfs(i, j + 1, t, s + ch)
            if j - 1 >= 0 and board[i][j - 1] != "#":
                dfs(i, j - 1, t, s + ch)
            board[i][j] = ch

        # 将word存入前缀树
        trie = {}
        for word in words:
            t = trie
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            t["end"] = 1

        m = len(board)
        n = len(board[0])
        res = []
        # 对board进行深度优先搜索
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, "")
        return res
