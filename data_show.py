import math

from constant.sensor_ID import SensorID
from sail.algorithm.shape_algorithm import ShapeAlgorithm
from sail.algorithm.sport_state_machine import SportStateConverter
from sail.sport import deep_squat
from util.filter import low_pass_filter
from util.plot_util import PlotUtil
from util.sensor_data_util import SensorDataUtil
from sail.seq_state import *

path = "data\\2019-05-05 22-41-37 深蹲5次.json"
sdu = SensorDataUtil(path)
pu = PlotUtil()

sensor = sdu.get_sensor(SensorID.HOST)

acc_data = sensor.acceleration.remove_abnormal(-20, 20).data
ori_data = sensor.orientation.remove_abnormal(-180, 180).data

ori_data_x = sensor.orientation.axis_x
ori_data_x_filtered = low_pass_filter(ori_data_x)

pu.plot(ori_data).plot(ori_data_x).show()

exit(123)
sa = ShapeAlgorithm()

ssc = SportStateConverter(deep_squat.sub_action_num)
ssc.set_table(deep_squat.sub_action_table_arm_ori)

for data in ori_data_x_filtered:
    seq_state, ind = sa.put_data(data)
    if seq_state != -1:
        print(seq_state, ind)
        sport_state = ssc.convert(seq_state)

        if sport_state == deep_squat.STAND_BY:
            print("当前是准备状态")
        if sport_state == deep_squat.SUB1_START:
            print("继续往下蹲！当前加速度:", acc_data[ind])
        if sport_state == deep_squat.SUB1_ONGOING:
            print("当前下蹲加速度：", acc_data[ind])
        if sport_state == deep_squat.SUB2_START:
            print("蹲到最低点，加速度:", acc_data[ind], "角度:", ori_data[ind])
        if sport_state == deep_squat.SUB2_ONGOING:
            print("上升！")
        if sport_state == deep_squat.ERR:
            print("出错了")

pu.plot(ori_data_x).plot(ori_data_x_filtered).show()
