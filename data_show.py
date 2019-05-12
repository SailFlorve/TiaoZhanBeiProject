from constant.sensor_ID import SensorID
from sail.algorithm.data_processor import paa
from util.plot_util import PlotUtil
from util.sensor_data_util import SensorDataUtil

path = "data\\2019-05-05 22-41-37 深蹲5次.json"
sdu = SensorDataUtil(path)
pu = PlotUtil()

sensor = sdu.get_sensor(SensorID.HOST)
sensor_ori = sensor.orientation

ori_data = sensor_ori.data
ori_data_x = sensor_ori.axis_x
ori_data_y = sensor_ori.axis_y
ori_data_z = sensor_ori.axis_z

for i in range(0, len(ori_data_x), 30):
    x_slice = ori_data_x[i:i + 200]
    pu.plot(x_slice).plot(paa(x_slice, 5), form='o-').show()
