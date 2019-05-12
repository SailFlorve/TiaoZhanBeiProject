import copy

import math
import numpy
from sklearn.decomposition import PCA


def sqrt_quadratic_sum(list):
    """
    将测量数据平方相加，再开根号\n
    :param list: 含有xyz数组的list:[[x1,y1,z1],[x2,y2,z2],...]
    :return: [sqrt(x1^2 + y1^2 + z1^2), sqrt(x2^2 + y2^2 + z2^2), ...]
    """
    result = []
    for child_list in list:
        result.append(math.sqrt(child_list[0] ** 2 + child_list[1] ** 2 + child_list[2] ** 2))
    return result


def fill_list(list, length, num=0):
    """
    把list用num填充至length长度
    :param list: 要填充的list
    :param num: 填充的数字
    :param length: 填充到的长度
    """
    if len(list) >= length:
        origin_list = copy.deepcopy(list)
        list.clear()
        for i in range(length):
            list.append(origin_list[i])

    else:
        for i in range(length - len(list)):
            list.append(num)


def zoom_list(data, length, value):
    """
    压缩list
    :param list:
    :param length:最大长度
    :param value: 最大值
    """

    list = data

    max_value = list[numpy.argmax(list)]

    if type(data) is numpy.ndarray:
        list = data.tolist()

    data_len = len(list)

    if max_value > value:
        zoom = value / max_value
        print(zoom)
        for i in range(len(list)):
            list[i] = list[i] * zoom

    if data_len <= length:
        return list

    diff = data_len - length
    step = int(data_len / diff)

    del_num = 0
    for i, val in enumerate(list):

        if i % (step + 1) == 0:
            del list[i - del_num]
            del_num += 1
    return list


def cut_invalid(data, value):
    """
    去除data中前后小于value的所有数据。
    如果list刚开始就大于value，一旦出现小于的时候再开始检测。+
    :param data:
    :param value:
    """
    if len(data) == 0:
        return []

    index = 0
    index_reverse = len(data)

    start = True

    if data[0] > value:
        start = False

    for i in range(len(data)):
        if start:
            if data[i] > value:
                index = i
                break
        else:
            if data[i] < value:
                start = True

    for r in list(range(0, len(data)))[::-1]:
        if data[r] > value:
            index_reverse = r
            break

    return data[index:index_reverse]


def pca(arr, dimen=1):
    result = PCA(n_components=dimen)
    new_arr = result.fit_transform(arr)
    data = numpy.reshape(new_arr, len(new_arr), -1)
    return data


def paa(arr, size):
    length = len(arr)
    if length == size:
        return arr
    else:
        if length % size == 99:
            return numpy.mean(numpy.hsplit(arr, size), axis=1)
        else:
            res = numpy.zeros(size)
            for i in range(length * size):
                idx = int(i / length)
                pos = int(i / size)
                res[idx] = res[idx] + arr[pos]
            for i in range(0, size):
                res[i] = res[i] / length
            return res


def sax(data, alphabet_size=4):
    if alphabet_size == 4:
        str_list = ''
        for i, val in enumerate(data):
            if val < -0.67:
                str_list += 'a'
            elif -0.67 < val < 0:
                str_list += 'b'
            elif 0 < val < 0.67:
                str_list += 'c'
            else:
                str_list += 'd'
        return str_list
    return None


def vector_cos(v1, v2):
    return v1.dot(v2) / (numpy.sqrt(v1.dot(v1)) * numpy.sqrt(v2.dot(v2)))


# 删除data中比max大和比min小的数字
def delete_max_min(data, max, min):
    result = []
    for i, d in enumerate(data):
        if max > data[i] > min:
            result.append(data[i])
    return numpy.array(result)
