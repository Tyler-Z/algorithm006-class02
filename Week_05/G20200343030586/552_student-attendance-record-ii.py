# 552. 学生出勤记录 II

class Solution:
    def checkRecord(self, n: int) -> int:
        condition = []
        def dfs(n,tmp):
            if n==0:
                condition.append(tmp)
                return
            for i in ['A','L','P']:
                dfs(n-1,tmp+i)
        dfs(n,'')
        res = 0
        for i in condition:
            count_A = i.count('A')
            count_LLL = i.count('LLL')
            if count_A <= 1 and count_LLL == 0:
                res+=1
        return res
