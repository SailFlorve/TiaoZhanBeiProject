from dataclasses import dataclass

import numpy as np


@dataclass
class Sensor:
    name: str
    accelerator_data: np.core.multiarray
    orientation_data: np.core.multiarray

