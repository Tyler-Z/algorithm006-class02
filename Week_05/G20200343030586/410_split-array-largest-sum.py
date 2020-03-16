# 410. 分割数组的最大值
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums),sum(nums)
        while left < right:
            mid = (left + right) // 2
            sums, cnt = 0, 1
            for i in nums:
                if sums + i > mid:
                    cnt += 1
                    sums = i
                else:
                    sums += i
            if cnt <= m:
                right = mid
            else:
                left = mid + 1
        return left
