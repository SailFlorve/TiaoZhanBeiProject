from typing import List

import matplotlib
import matplotlib.pyplot as plt


class PlotUtil:
    data_list: List = []
    label_list = []
    title_list = []
    form_list = []

    plot_num: int = 0

    def __init__(self):
        pass

    def plot(self, data, label=None, title=None, form=None):
        self.data_list.append(data)
        self.label_list.append(label)
        self.title_list.append(title)
        self.form_list.append('-' if form is None else form)
        self.plot_num += 1
        return self

    def show(self, row=None, column=None):
        row = self.plot_num if row is None else row
        column = 1 if column is None else column

        plt.figure()
        for i, data in enumerate(self.data_list):
            sp: matplotlib.pyplot = plt.subplot(row, column, i + 1)
            sp.plot(self.data_list[i], self.form_list[i], label=self.label_list[i])
            sp.legend()
            plt.title(self.title_list[i])

        plt.show()

        self.clear()

    def clear(self):
        self.data_list.clear()
        self.label_list.clear()
        self.form_list.clear()
        self.title_list.clear()
        self.plot_num = 0
