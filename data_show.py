import math

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

path = "data\\2019-05-05 22-41-37 深蹲5次.json"
sdu = SensorDataUtil(path)
pu = PlotUtil()

sensor = sdu.get_sensor(SensorID.HOST)

acc_data = sensor.acceleration.remove_abnormal(-20, 20).data
ori_data = sensor.orientation.remove_abnormal(-180, 180).data

acc_data_x = sensor.acceleration.axis_x
acc_data_y = sensor.acceleration.axis_y
acc_data_z = sensor.acceleration.axis_z

acc_data_x_filtered = low_pass_filter(acc_data_x)
acc_data_y_filtered = low_pass_filter(acc_data_y)
acc_data_z_filtered = low_pass_filter(acc_data_z)

ori_data_x = sensor.orientation.axis_x
ori_data_x_filtered = low_pass_filter(ori_data_x)

pu.plot(acc_data).show()
pu.plot(acc_data_x_filtered).plot(acc_data_y_filtered).plot(acc_data_z_filtered).show_together()

sa = ShapeAlgorithm()

ssc = SportStateConverter(deep_squat.sub_action_num)
ssc.set_table(deep_squat.sub_action_table_arm_ori)

delay_list = []

for i, data in enumerate(ori_data_x_filtered):
    seq_state, ind = sa.put_data(data)

    if seq_state != -1:
        print(seq_state, ind, i)
        sport_state = ssc.convert(seq_state)
        print("子动作: ", end='')

        if sport_state == deep_squat.STAND_BY:
            print("站立")
        if sport_state == deep_squat.SUB1_START:
            print("开始下蹲过程", acc_data[ind])
        if sport_state == deep_squat.SUB1_ONGOING:
            print("下蹲过程")
        if sport_state == deep_squat.SUB2_START:
            print("开始起立过程")
        if sport_state == deep_squat.SUB2_ONGOING:
            print("起立过程")
        if sport_state == deep_squat.ERR:
            print("出错了")

pu.plot(ori_data_x).plot(ori_data_x_filtered).show()

delay_list = [2, 5, 8, 11, 14, 44, 14, 14, 44, 14, 14, 14, 44, 14, 14, 44, 14, 14, 44, 14, 14, 14, 44, 14, 14, 44, 14,
              14, 44, 14, 14, 44, 14, 14, 2, 5, 8, 11, 14, 44, 14, 14, 44, 14, 14, 14, 44, 14, 14, 44, 14, 14, 44, 14,
              14, 44, 14, 14, 14, 44, 14, 14, 44, 14, 14, 44, 14, 14]
plt.hist(delay_list, bins=10)
plt.ylabel("")
plt.xlabel("data num")
plt.legend()
plt.show()
