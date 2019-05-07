from dataclasses import dataclass

import numpy as np

from constant.sensor_ID import SensorID


# 此类表示一个传感器
from entry.sensor_data_sequence import SensorDataSequence


@dataclass
class Sensor:
    name: str
    acceleration: SensorDataSequence
    orientation: SensorDataSequence
