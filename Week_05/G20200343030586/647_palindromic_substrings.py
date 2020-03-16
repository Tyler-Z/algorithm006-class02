"""
647. 回文子串
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:
输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".

示例 2:
输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:

输入的字符串长度不会超过1000。
"""

class Solution(object):
    def countSubstrings(self, S):
        N = len(S)
        ans = 0
        for center in xrange(2*N - 1):
            left = center / 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans