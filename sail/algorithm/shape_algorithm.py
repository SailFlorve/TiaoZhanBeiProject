from typing import List

import numpy as np

from sail.algorithm.data_processor import paa, pca
from util.plot_util import PlotUtil

from sail.seq_state import *


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

    pu = PlotUtil()

    def __init__(self):
        pass

    def put_data(self, d) -> (int, int):
        self.data.append(d)
        if len(self.data) % self.process_threshold == 0:
            data_slice = self.get_window(self.data)
            return self.process(data_slice)
        else:
            return -1, -1

    def get_window(self, data):
        data_len = len(data)
        window_start = data_len - self.window_size
        data_slice = data[window_start:data_len] if data_len >= self.window_size else data
        return data_slice

    def process(self, data_slice) -> (int, int):
        paa_result = paa(data_slice, self.paa_size)

        state = self.judge_state(paa_result)

        self.pu.plot(data_slice).plot(paa_result, 'o-').show()

        if state == MINIMUM_VALUE or state == MAXIMUM_VALUE:
            index = self.get_index_in_data(len(data_slice), self.paa_size - 2)
        else:
            index = self.get_index_in_data(len(data_slice), self.paa_size - 1)

        return state, index

    def judge_state(self, paa_result) -> int:
        var = np.var(paa_result)
        last_index = len(paa_result) - 1

        if var <= self.static_var:
            return STATIC

        if paa_result[last_index] < paa_result[last_index - 1]:
            if paa_result[last_index - 2] < paa_result[last_index - 1]:
                return MAXIMUM_VALUE
            else:
                return DECREASING

        if paa_result[last_index] > paa_result[last_index - 1]:
            if paa_result[last_index - 2] > paa_result[last_index - 1]:
                return MINIMUM_VALUE
            else:
                return INCREASING

    # 根据PAA的index获取数据原来的index
    def get_index_in_data(self, window_size, paa_index) -> int:
        split_num = int(window_size / self.paa_size)
        index = len(self.data) - (self.paa_size - paa_index - 1 + 0.5) * split_num
        return int(index)
