import numpy as np


class SensorDataSequence:
    data: np.ndarray

    axis_x: np.ndarray
    axis_y: np.ndarray
    axis_z: np.ndarray

    def __init__(self, data):
        self.data = data
        self.generate_axis(data)

    def generate_axis(self, data):
        self.axis_x = data[:, 0:1].reshape(len(data))
        self.axis_y = data[:, 1:2].reshape(len(data))
        self.axis_z = data[:, 2:3].reshape(len(data))

    def remove_abnormal(self, min_v, max_v):
        data = np.clip(self.data, min_v, max_v)
        self.data = data
        self.generate_axis(data)
        return self
