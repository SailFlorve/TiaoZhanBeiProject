from constant.sensor_ID import SensorID
from sail.algorithm.data_processor import *
from sail.algorithm.shape_algorithm import ShapeAlgorithm
from util.filter import low_pass_filter
from util.plot_util import PlotUtil
from util.sensor_data_util import SensorDataUtil

path = "data\\2019-05-05 22-41-37 深蹲5次.json"
sdu = SensorDataUtil(path)
pu = PlotUtil()

sensor = sdu.get_sensor(SensorID.HOST)

acc_data = sensor.acceleration.remove_abnormal(-20, 20).data
ori_data = sensor.orientation.remove_abnormal(-180, 180).data

acc_pca = low_pass_filter(pca(acc_data))
ori_pca = low_pass_filter(pca(ori_data))

pu.plot(acc_data).plot(acc_pca).plot(ori_data).plot(ori_pca).show()

sa = ShapeAlgorithm()

for data in numpy.nditer(ori_pca):
    res, ind = sa.put_data(data)
    if res != -1:
        print(res, ind)
        if ind is not None:
            print(sa.data[ind])

pu.plot(ori_pca).plot(acc_pca).show_together()
