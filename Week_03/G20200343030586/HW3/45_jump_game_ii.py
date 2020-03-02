"""
45. 跳跃游戏 II
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        inde = 0
        n = 0
        i = 0

        if len(nums) == 1 or not nums:
            return 0
        while True:
            ax = nums[i]
            if nums[i] + i >= len(nums) - 1:
                return n + 1
            for (j, k) in enumerate(range(i, nums[i] + i + 1)):

                if nums[k] + j > ax:
                    ax = nums[k] + j
                    inde = j

            if inde == 0:
                inde = nums[i]
            i += inde
            n += 1

            if i >= len(nums) - 1:
                return n
            inde = 0
