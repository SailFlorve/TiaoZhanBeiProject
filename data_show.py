from constant.sensor_ID import SensorID
from util.filter import low_pass_filter
from util.sensor_data_util import SensorDataUtil
from matplotlib import pyplot as plt

path = "data\\2019-05-05 22-41-37 深蹲5次.json"

# 初始化Util
util = SensorDataUtil(path)

# 打印数据信息
print(util)

# 绘制该传感器所有轴的图
util.plot(SensorID.SLAVE_3)

plt.figure()

# 获得从机3的加速度
slave_3_acc = util.get_sensor(SensorID.SLAVE_3).acceleration_data

plt.subplot(311)
plt.plot(slave_3_acc)
plt.title("Salve Sensor 3 Acceleration All Axis")

# 获得从机3加速度z轴
slave_3_acc_z = util.get_axis(SensorID.SLAVE_3, SensorID.AXIS_Z, SensorID.DATA_ACCELERATOR)

plt.subplot(312)
plt.plot(slave_3_acc_z)
plt.title('Salve Sensor 3 Acceleration Z Axis')

# 对从机3加速度z轴进行滤波
slave_3_acc_z_filtered = low_pass_filter(slave_3_acc_z)

plt.subplot(313)
plt.plot(slave_3_acc_z)
plt.plot(slave_3_acc_z_filtered)
plt.title("Slave Sensor 3 Acceleration Z Axis Filtered")

plt.show()