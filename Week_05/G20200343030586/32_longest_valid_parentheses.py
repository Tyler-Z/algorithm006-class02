"""
32. 最长有效括号
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res=[]
        stack=[]
        for i in range(len(s)):
            if(stack and s[i]==")"):
                res.append(stack.pop())
                res.append(i)
            if(s[i]=="("):
                stack.append(i)
        #print(res)
        res.sort()
        max_len=0
        i=0
        while(i<len(res)-1):
            tmp=i
            while(i<len(res)-1 and res[i+1]-res[i]==1):
                i+=1
            max_len=max(max_len,i-tmp+1)
            i+=1
        return max_len
