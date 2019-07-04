from data_show import *
import matplotlib.pyplot as plt
import numpy as np

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

delay_list = [2, 5, 8, 11, 12, 44, 13, 14, 44, 10, 12, 13, 40, 15, 13, 44, 11, 12, 41, 14, 14, 14, 40, 12, 12, 40, 11,
              15, 41, 14, 14, 42, 14, 14, 2, 5, 8, 11, 14, 44, 13, 13, 44, 13, 13, 14, 44, 13, 14, 44, 14, 12, 44, 14,
              14, 44, 14, 14, 14, 44, 14, 14, 44, 14, 14, 44, 14, 14]
delay_list = np.array(delay_list) / 40
plt.plot(delay_list, 'o-')
plt.ylabel("Delay /s")
plt.ylim(0, 2)
plt.legend()
plt.show()


def draw_bar(labels, quants):
    width = 0.4
    ind = np.linspace(1, 5, 5)
    # make a square figure
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    # Bar Plot
    ax.bar(ind - width / 2, quants, width, color='GRAY')
    # Set the ticks on x-axis
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    # labels
    ax.set_xlabel('ACTION PROCESS')
    ax.set_ylabel('ACCURACY')
    plt.show()
    plt.close()


labels = ['STAND', 'SQUAT-START', 'SQUAT-ING', 'RISE-START', 'RISE-ING']

quants = [98.55, 96.67, 94.55, 97.77, 96.90]

draw_bar(labels, quants)
