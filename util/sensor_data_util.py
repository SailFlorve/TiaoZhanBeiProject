from constant.sensor_ID import SensorID
from entry.sensor import Sensor
from entry.sensor_data import SensorData
from util.json_parser import JsonParser
import numpy as np
from matplotlib import pyplot as plt


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
        plt.plot(self.sensor_data.sensor_dict[sensor_id].accelerator_data)
        plt.show()

        plt.plot(self.sensor_data.sensor_dict[sensor_id].orientation_data)
        plt.show()


if __name__ == '__main__':
    path = "E:\\Documents\\资料\\MLDA\\硬件数据\\2018-07-19 21-40-54 深蹲0次.json"
    u = SensorDataUtil(path)
    print(u)
    u.plot(SensorID.HOST)
