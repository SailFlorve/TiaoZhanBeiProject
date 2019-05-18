from sail.algorithm.shape_algorithm import ShapeAlgorithm
from sail.algorithm.sport_state_machine import SportStateConverter
from sail.seq_state import *
from sail.sport import deep_squat


class ActionRecognizeAlgorithm:
    sa: ShapeAlgorithm
    ssc: SportStateConverter

    def __init__(self, sub):
        sa = ShapeAlgorithm()
        ssc = SportStateConverter(sub)
