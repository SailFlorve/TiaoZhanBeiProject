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

# 绘制该传感器所有轴的图
sdu.plot(SensorID.HOST)

plt.figure()

sensor_host = sdu.get_sensor(SensorID.SLAVE_3)

# 获得主机的加速度
host_acc_seq = sensor_host.acceleration

# 三轴
host_acc_data = host_acc_seq.data
# x,y,z
host_acc_x = host_acc_seq.axis_x()
host_acc_y = host_acc_seq.axis_y()
host_acc_z = host_acc_seq.axis_z()

plt.plot(host_acc_x, label='x')
plt.plot(host_acc_y, 'o-', label='y')
plt.plot(host_acc_z, label='z')

plt.legend()
plt.show()

host_acc_z_filtered = low_pass_filter(host_acc_z, weight=0.08)
plt.plot(host_acc_z_filtered)
plt.plot(host_acc_z)
plt.show()

host_acc_z_filtered_diff = np.diff(host_acc_z_filtered)

plt.plot(host_acc_z_filtered)
plt.plot(low_pass_filter(host_acc_z_filtered_diff))
print(host_acc_z_filtered)
print(host_acc_z_filtered_diff)
plt.show()
