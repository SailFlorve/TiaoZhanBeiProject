from constant.sensor_ID import SensorID
from util.filter import low_pass_filter
from util.plot_util import PlotUtil
from util.sensor_data_util import SensorDataUtil
from matplotlib import pyplot as plt
import numpy as np

path = "data\\2019-05-05 22-41-37 深蹲5次.json"
sdu = SensorDataUtil(path)
pu = PlotUtil()

sensor = sdu.get_sensor(SensorID.HOST)
sensor_acc = sensor.acceleration

acc_x = sensor_acc.axis_x()
acc_y = sensor_acc.axis_y()

pu.plot(acc_x, 'x', 'x data').plot(acc_y, title='y data').plot(sensor_acc.data).show(2, 1)
pu.plot(acc_x).show()
