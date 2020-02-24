# 49. 字母异位词分组


"""
# 方法一：排序数组分类（Categorize by Sorted String）
import collections

class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()


# 方法二：按计数分类（Categorize by Count）
class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def convert(s):
            res = [0]*26
            for char in s:
                res[ord(char)-ord('a')] += 1
            return tuple(res)
        rec = {}
        res = []
        for s in strs:
            t = convert(s)
            if t in rec:
                res[rec[t]].append(s)
            else:
                res.append([s])
                rec[t] = len(res)-1
        return res
