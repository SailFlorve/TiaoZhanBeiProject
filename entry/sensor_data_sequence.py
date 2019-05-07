from dataclasses import dataclass

import numpy as np


@dataclass
class SensorDataSequence:
    data: np.core.multiarray

    def axis_x(self):
        return self.data[:, 0:1]

    def axis_y(self):
        return self.data[:, 1:2]

    def axis_z(self):
        return self.data[:, 2:3]
