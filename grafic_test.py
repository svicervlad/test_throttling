import os
import matplotlib.pyplot as plt
from throttling import PATH_RESULT


def _grafic(times, array, name):
    plt.rcParams["figure.figsize"] = (20, 4)
    plt.plot(times, array)
    plt.ylabel(name)
    plt.xlabel("seconds")
    plt.savefig(format='png', fname=os.path.join(PATH_RESULT, f'{name}.png'),
                orientation="landscape")
    plt.clf()
    plt.cla()


def grafic(array, name):
    """
    Создает графики для частоты, загружености и температуры процессора
    принимает словарь cpu_info() и имя теста
    """
    len_array = [x for x in range(len(array))]
    freq = [x["cpu_info"]["cpu_freq"] for x in array]
    temp = [x["cpu_info"]["cpu_temp"] for x in array]
    load = [x["cpu_info"]["cpu_load"] for x in array]
    _grafic(len_array, freq, f'{name}_freq')
    _grafic(len_array, temp, f'{name}_temp')
    _grafic(len_array, load, f'{name}_load')
