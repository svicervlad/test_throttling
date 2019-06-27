import os
import numpy as np

MAIN_PATH = os.path.abspath(os.path.join(__file__, os.pardir))
PATH_RESULT = os.path.join(MAIN_PATH, "result")


def trottling(array, name):
    """
    вычисляет сколько времени в процентах процессор держался на одной частоте
    которая выше среднего значения
    """
    freq = [x["cpu_info"]["cpu_freq"] for x in array]
    sec = 0
    for x in range(len(freq)):
        if not x == len(freq) - 1:
            if freq[x + 1] >= freq[x] and freq[x] > np.mean(freq):
                sec += 1

    p_trottling = round(sec / len(freq) * 100, 1)
    test_result = f'test {name}\nmax freq: {max(freq)}\n' + \
                  f'average freq: {np.mean(freq)}\ntrottling: {p_trottling}%\n'
    with open(os.path.join(PATH_RESULT, f"trottling - {name}.txt"), 'w') as f:
        f.write(test_result)
