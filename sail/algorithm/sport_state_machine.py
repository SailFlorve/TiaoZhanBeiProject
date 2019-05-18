import numpy as np

"""
StateTable: 2d array
Row: Sport state
Column: Next Sequence state
Value: State transformed to

                STATIC  DECREASING  INCREASING  MINIMUM MAXIMUM
STAND_BY(0)     
SUB1_START(1)
SUB1_ONGOING(2)
SUB2_START(3)
SUB2_ONGOING(4)
...

"""


class SportStateConverter:
    state_convert_table: np.core.multiarray
    sub_action_num: int
    current: int

    def __init__(self, sub):
        self.sub_action_num = sub
        self.state_convert_table = np.zeros([sub * 2 + 1, 5])
        self.current = 0

    def set_table(self, table):
        self.state_convert_table = table

    def convert(self, next_seq_state) -> int:
        self.current = self.state_convert_table[self.current, next_seq_state]
        return self.current
