"""
22. 括号生成
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        dp = [None for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            cur = []
            for j in range(i):
                left = dp[j]
                right = dp[i - j - 1]
                for s1 in left:
                    for s2 in right:
                        cur.append("(" + s1 + ")" + s2)
            dp[i] = cur
        return dp[n]

