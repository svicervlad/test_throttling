"""
Сдесь находятся тесты в виде функций
"""
from threading import Thread
# from multiprocessing.dummy import Pool as ThreadPool
# from psutil import cpu_count
import tests.build_test as kernel
from tests.fibonacci import fibonacci
from measure import measure_test, clock_test


NUM_FIB = 43


def core_test(func, *arg):
    """
    принимает функцию и аргументы.
    возвращает время выполненние функции, состояние процессора каждые 1 секунд
    во время работы функции. Вывод в виде списка
    [время работы, состояние процессора]
    """
    stage = 0
    list_stage = []
    test_time = []

    def test(func, *arg):
        time_func = measure_test(func, *arg)
        nonlocal stage, test_time
        stage = 1
        test_time = time_func

    test = Thread(target=test, args=(func, *arg))
    test.start()
    while stage == 0:
        list_stage.append(clock_test())
        # поскольку данные собираются секунду таймаут не нужен
    return [test_time, list_stage]


def kernel_test():
    """
    Тестирует сборку ядра linux,
    возвращает словарь в виде:
    {"get_kernel_test": core_test, "extract_kernel_test": core_test,
    "make_kernel_test": core_test}
    """
    get_kernel_test = core_test(kernel.get_kernel)
    extract_kernel_test = core_test(kernel.extract_kernel)
    make_kernel_test = core_test(kernel.make_kernel)
    return {"get_kernel_test": get_kernel_test, "extract_kernel_test":
            extract_kernel_test, "make_kernel_test": make_kernel_test}


def single_core_fibonacci():
    """
    Тестирует функцию фибоначи
    """
    return core_test(fibonacci, NUM_FIB)
