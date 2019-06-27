"""
Функциии для определения времени выполненния
"""
from time import time
from cpu_info import cpu_params


def measure_test(func, *arg):
    """
    принимает функцию, и возвращает время старта, окончания работы,
    время потраченное на работу функции.
    Пример: measure_test(func, arg)
    """
    before = time()
    func(*arg)
    after = time()
    deltatime = after - before
    info = {"start_time": before, "end_time": after, "time": deltatime}
    return info


def clock_test():
    """
    собирает в словарь замер времени и состояния процессора
    """
    info = {"time": time(), "cpu_info": cpu_params()}
    return info
