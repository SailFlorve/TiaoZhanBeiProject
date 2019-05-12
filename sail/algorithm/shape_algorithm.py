from typing import List

import numpy as np

from sail.algorithm.data_processor import paa
from util.plot_util import PlotUtil

STATIC = 0  # 静止/站立
DECREASING = 1  # 数值下降
INCREASING = 2  # 数值上升
MINIMUM_VALUE = 3  # 出现极小值
MAXIMUM_VALUE = 4  # 出现极大值


class ShapeAlgorithm:
    sub_actions: List
    sub_action_num: int
    sub_action_feature: List
    sub_action_boundary: List

    data: List = []

    process_threshold: int = 30
    paa_size: int = 5  # 必须>3
    window_size: int = 150
    static_var = 1

    def __init__(self):
        pass

    def put_data(self, d):
        self.data.append(d)
        data_slice = self.get_window()
        if len(self.data) % self.process_threshold == 0:
            return self.process(data_slice)
        else:
            return -1, -1

    def get_window(self):
        data_len = len(self.data)
        window_start = data_len - self.window_size
        data_slice = self.data[window_start:data_len] if data_len >= self.window_size else self.data
        return data_slice

    def judge_state(self, paa_result):
        var = np.var(paa_result)
        last_index = len(paa_result) - 1
        if var <= self.static_var:
            return STATIC, None
        if paa_result[last_index] < paa_result[last_index - 1]:
            if paa_result[last_index - 2] < paa_result[last_index - 1]:
                return MINIMUM_VALUE, self.get_index_in_data(3)
            else:
                return DECREASING, None

        if paa_result[last_index] > paa_result[last_index - 1]:
            if paa_result[last_index - 2] > paa_result[last_index - 1]:
                return MAXIMUM_VALUE, self.get_index_in_data(3)
            else:
                return INCREASING, None

    def process(self, data_slice):

        paa_result = paa(data_slice, self.paa_size)
        pu = PlotUtil()
        # pu.plot(data_slice).plot(paa_result, 'o-').show()

        state, index = self.judge_state(paa_result)
        return state, index

    def get_index_in_data(self, paa_index):
        split_num = int(self.window_size / self.paa_size)
        return len(self.data) - (self.paa_size - paa_index - 1) * split_num


if __name__ == "__main__":
    sub_actions = ["下蹲", '站立']
    sub_actions_num = 2
    sub_action_feature = [[DECREASING], [INCREASING]]
    sub_action_boundary = [[DECREASING, MINIMUM_VALUE], [INCREASING, MAXIMUM_VALUE]]

    ag = ShapeAlgorithm()