from constant.sensor_ID import SensorID
from sail.algorithm.data_processor import *
from sail.algorithm.shape_algorithm import ShapeAlgorithm
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

algorithm = ShapeAlgorithm()

last_state = -1
for data in ori_data_x:
    if data > 200 or data < -200:
        continue
    state, index = algorithm.put_data(data)
    if state != -1:
        print(state, "index:", index)

pu.plot(ori_data_x).show()

exit(9)

data_queue = []

pu.plot(ori_data_x).show()

for data in ori_data_x:
    data_queue.append(data)
    if len(data_queue) % 30 != 0:
        continue
    data_len = len(data_queue)
    if data_len < 100:
        data_slice = data_queue
    else:
        data_slice = data_queue[data_len - 100:data_len]

    paa_res = paa(data_slice, 5)
    print(numpy.var(paa_res))
    pu.plot(data_slice).plot(paa_res, form="o-").show()
