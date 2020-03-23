"""
433. 最小基因变化
一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。

假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。

例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。

与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。

现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。

注意:

起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
所有的目标基因序列必须是合法的。
假定起始基因序列与目标基因序列是不一样的。
"""


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1

        dictionary = {"A": "CGT", "C": "AGT", "G": "ACT", "T": "ACG"}
        front_queue = {start}
        end_queue = {end}
        step = 0

        while front_queue:
            step += 1
            next_front = set()

            for word in front_queue:
                for i in range(len(word)):
                    for c in dictionary.get(word[i]):
                        new_word = word[:i] + c + word[i + 1:]
                        if new_word in end_queue:  # 相遇
                            return step
                        if new_word in bank:
                            next_front.add(new_word)
                            bank.remove(new_word)

            front_queue = next_front

            if len(end_queue) < len(front_queue):
                front_queue, end_queue = end_queue, front_queue

        return -1