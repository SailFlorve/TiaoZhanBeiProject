import math

from pandas import Series
from partd import pandas

from constant.sensor_ID import SensorID
from sail.algorithm.shape_algorithm import ShapeAlgorithm
from sail.algorithm.sport_state_machine import SportStateConverter
from sail.sport import deep_squat
from util.filter import low_pass_filter
from util.plot_util import PlotUtil
from util.sensor_data_util import SensorDataUtil
from sail.seq_state import *
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose

path = "data\\2019-05-05 22-41-37 深蹲5次.json"
sdu = SensorDataUtil(path)
pu = PlotUtil()

sensor = sdu.get_sensor(SensorID.HOST)

acc_data = sensor.acceleration.remove_abnormal(-20, 20).data
ori_data = sensor.orientation.remove_abnormal(-180, 180).data

acc_data_x = sensor.acceleration.axis_x
acc_data_y = sensor.acceleration.axis_y
acc_data_z = sensor.acceleration.axis_z

ori_data_x = sensor.orientation.axis_x.data

ori_data_x_filtered = low_pass_filter(sensor.orientation.axis_x.data)

print(acc_data_x.tolist())
acc_data_x_filtered = low_pass_filter(acc_data_x)


pu.plot(acc_data_x).plot(acc_data_x_filtered).show_together()

exit(1)

acc_data_x_df= Series(acc_data_x)
decomposition = seasonal_decompose(acc_data_x_df)
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid
decomposition.plot()
plt.show()
