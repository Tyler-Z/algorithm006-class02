# 403. 青蛙过河
class Solution:
    def canCross(self, stones):
        if stones[1] > 1:
            return False
        self.stones = stones

        #: `pos_dict`字典 {第i块石头所在的格子位置：i}
        self.pos_dict = { s[1]:s[0] for s in enumerate(stones)}

        #: 集合cut用于剪枝，集合元素为`tuple(当前石头i，要走的步数s)`。
        #: 如果在cut集合，说明在当前石头，走s步到最后是走不通的，应该放弃。
        self.cut = set()

        end = len(stones)-1
        #: 假设前一步走了0步，现在在第一块石头上。
        return self.traverse(0, 0, end)

    def traverse(self, pre_step, current, end):
        """前一次走了`pre_step`步，当前在stones中第`current`块石头上，目标是到达第`end`块石头。"""
        if current == end:
            #: 到达end
            return True

        if current < end:
            #: 三叉搜索，pre_step-1,pre_step,pre_step+1
            for step in range(pre_step-1, pre_step+2):
                if step>0 and (current,step) not in self.cut:
                    #: `nexp_pos`表示如果从第`current`块石头起跳`step`步到达的格子位置。
                    next_pos = self.stones[current] + step
                    #: 如果该位置`next_pos`有石头，就跳上去，递归。
                    next_stone_index = self.pos_dict.get(next_pos)
                    if next_stone_index:
                        r = self.traverse(step, next_stone_index, end)
                        if r != -1:
                            return r
                        self.cut.add((current, step))  # 记录下来，此路不通。

        if current == 0 :
            # 当无法到达end时，最后会回到第一块石头（树的根）
            return False
        else:
            # 无石头能跳，该路径走到头了
            return -1