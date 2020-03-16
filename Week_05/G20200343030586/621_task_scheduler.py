"""
621. 任务调度器

给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。
然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。
示例 1：
输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
注：

任务的总个数为 [1, 10000]。
n 的取值范围为 [0, 100]。
"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        dict1 = {}
        for i in tasks:
            dict1[i] = dict1.get(i, 0) + 1
        min_time = 0
        max_task = max(dict1, key=dict1.get)
        # 完成次数最多的任务需要的任务时间为 (count - 1) * (n + 1) + 1
        min_time = (dict1[max_task] - 1) * (n + 1) + 1
        for k, v in dict1.items():
            # 找到相同任务次数的其他任务
            if v == dict1[max_task] and k != max_task:
                min_time += 1
        # 任务总时间必须大于数组长度，如果 任务种类-1>n，说明可以直接依次完成任务，例如ABCDABC
        if min_time < len(tasks):
            min_time = len(tasks)
        return min_time
