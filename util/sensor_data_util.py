import numpy as np
from matplotlib import pyplot as plt

from constant.sensor_ID import SensorID
from entry.sensor import Sensor
from entry.sensor_data_sequence import SensorDataSequence
from entry.sensor_data_set import SensorDataSet
from util.json_parser import JsonParser


class SensorDataUtil:
    sensor_data: SensorDataSet = None

    def __init__(self, path: str = None):
        if path is not None:
            self.load(path)

    def __str__(self):
        result = "SensorDataUtil\n"
        result += str(self.sensor_data)
        return result

    def load(self, json_path):
        json_parser = JsonParser(json_path, is_path=True)
        sensor_data_json_parser = JsonParser(json_parser.get("sensorData"), is_path=False)

        sensor_data = SensorDataSet()
        sensor_data.input_times = json_parser.get("inputTimes")
        sensor_data.action_type = json_parser.get("type")

        for i in range(0, len(sensor_data_json_parser.json_dict), 2):
            sub_dict_acc = sensor_data_json_parser.index(i)
            sub_dict_gyro = sensor_data_json_parser.index(i + 1)
            sensor = Sensor(
                SensorID.int_to_ID_dict[int(i / 2) + 1],
                SensorDataSequence(np.array(sub_dict_acc["data"])),
                SensorDataSequence(np.array(sub_dict_gyro["data"]))
            )
            sensor_data.add_sensor(sensor)

        self.sensor_data = sensor_data

    def plot(self, sensor_id: str):
        plt.figure()
        plt.subplot(211)
        plt.plot(self.sensor_data.sensor_dict[sensor_id].acceleration.data)
        plt.title('Acceleration')
        plt.subplot(212)
        plt.plot(self.sensor_data.sensor_dict[sensor_id].orientation.data, label='Orientation')
        plt.title("Orientation")
        plt.legend()
        plt.show()

    def get_sensor(self, sensor_id: str) -> Sensor:
        return self.sensor_data.get_sensor(sensor_id)


if __name__ == '__main__':
    pass
