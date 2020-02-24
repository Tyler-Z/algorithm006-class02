# 47. 全排列 II

"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

# 46题，用nums[:i] + nums[i+1:] 巧妙避免了重复利用的问题
# 用nums[i]==nums[i-1]，进行剪枝



class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 数组先排序
        self.res = []
        self.recur(nums,[])
        return self.res

    def recur(self,nums,temp):
        if nums == []:
            self.res.append(temp)
            return
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]: #每当进入新的构成，先考虑该构成的首字符是否和上一个一样。
                continue
            self.recur(nums[:i]+nums[i+1:],temp+[nums[i]]) #nums[:i]+nums[i+1:] 避免了重复利用。

