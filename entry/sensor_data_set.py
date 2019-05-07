from typing import Dict

from entry.sensor import Sensor


# 此类保存四个传感器的数据
class SensorDataSet:
    input_times: int = 0
    action_type: str = None
    sensor_dict: Dict[str, Sensor] = {}

    def __init__(self):
        pass

    def add_sensor(self, sensor: Sensor):
        self.sensor_dict[sensor.name] = sensor

    def __str__(self):
        result = "inputTimes: " + str(self.input_times) + "\n"
        result += "actionType: " + self.action_type + "\n"
        result += "Sensor: \n" + str(self.sensor_dict) + "\n"
        return result

    def get_sensor(self, sensor_id: str) -> Sensor:
        return self.sensor_dict[sensor_id]
