from dataclasses import dataclass

import numpy as np


class SensorDataSequence:
    data: np.ndarray

    axis_x: np.ndarray
    axis_y: np.ndarray
    axis_z: np.ndarray

    def __init__(self, data):
        self.data = data
        self.axis_x = data[:, 0:1]
        self.axis_y = data[:, 1:2]
        self.axis_z = data[:, 2:3]
