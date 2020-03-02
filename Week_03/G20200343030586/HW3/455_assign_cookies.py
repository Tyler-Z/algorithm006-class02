"""
455. 分发饼干

假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

"""


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        res = 0
        g.sort()
        s.sort()

        g_length = len(g)
        s_length = len(s)

        i = 0
        j = 0
        while i < g_length and j < s_length:
            if g[i] <= s[j]:
                # 可以满足胃口，把小饼干喂给小朋友
                res += 1
                i += 1
                j += 1
            else:
                # 不满足胃口，查看下一块小饼干
                j += 1

        return res

