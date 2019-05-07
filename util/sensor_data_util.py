import numpy as np
from matplotlib import pyplot as plt

from constant.sensor_ID import SensorID
from entry.sensor import Sensor
from entry.sensor_data import SensorData
from util.json_parser import JsonParser


class SensorDataUtil:
    sensor_data: SensorData = None

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

        sensor_data = SensorData()
        sensor_data.input_times = json_parser.get("inputTimes")
        sensor_data.action_type = json_parser.get("type")

        for i in range(0, len(sensor_data_json_parser.json_dict), 2):
            sub_dict_acc = sensor_data_json_parser.index(i)
            sub_dict_gyro = sensor_data_json_parser.index(i + 1)
            sensor = Sensor(
                SensorID.int_to_ID_dict[int(i / 2) + 1],
                np.array(sub_dict_acc["data"]),
                np.array(sub_dict_gyro["data"])
            )
            sensor_data.add_sensor(sensor)

        self.sensor_data = sensor_data

    def plot(self, sensor_id: str):
        plt.figure()
        plt.subplot(211)
        plt.plot(self.sensor_data.sensor_dict[sensor_id].acceleration_data)
        plt.title('Acceleration')
        plt.subplot(212)
        plt.plot(self.sensor_data.sensor_dict[sensor_id].orientation_data, label='Orientation')
        plt.title("Orientation")
        plt.legend()
        plt.show()

    def get_sensor(self, sensor_id: str) -> Sensor:
        return self.sensor_data.get_sensor(sensor_id)

    def get_axis(self, sensor_id: str, axis: int, data_type: int):
        sensor = self.get_sensor(sensor_id)
        if data_type == SensorID.DATA_ACCELERATOR:
            return sensor.acceleration_data[:, axis:axis + 1]
        elif data_type == SensorID.DATA_ORIENTATION:
            return sensor.orientation_data[:, axis:axis + 1]


if __name__ == '__main__':
    pass
