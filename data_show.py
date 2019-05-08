from constant.sensor_ID import SensorID
from util.filter import low_pass_filter
from util.sensor_data_util import SensorDataUtil
from matplotlib import pyplot as plt
import numpy as np

path = "data\\2019-05-05 22-41-37 深蹲5次.json"

# 初始化Util
sdu = SensorDataUtil(path)

# 打印数据信息
print(sdu)

sensor_host = sdu.get_sensor(SensorID.SLAVE_3)

# 获得主机的加速度
host_acc_seq = sensor_host.acceleration

# 三轴
host_acc_data = host_acc_seq.data
# x,y,z
host_acc_x = host_acc_seq.axis_x()
host_acc_y = host_acc_seq.axis_y()
host_acc_z = host_acc_seq.axis_z()

host_ori_data = sensor_host.orientation.data
ori_x = sensor_host.orientation.axis_x
ori_y = sensor_host.orientation.axis_y
ori_z = sensor_host.orientation.axis_z

host_acc_x_fixed = (host_acc_x * np.cos(ori_x))
host_acc_y_fixed = (host_acc_y * np.cos(ori_y))
host_acc_z_fixed = (host_acc_z * np.cos(ori_z))

plt.plot(host_acc_x_fixed)
plt.plot(host_acc_y_fixed)
plt.plot(host_acc_z_fixed)

plt.show()