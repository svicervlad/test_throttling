"""
Информация о процессоре:
+ частота ядра
+ температура
+ загруженость ядра в процентах
"""

from psutil import cpu_percent, cpu_freq


def _cpu_temp():
    """
    получает температуру процессора
    """
    return int(open('/sys/class/thermal/thermal_zone0/temp').readline())/1000


def cpu_params():
    """
    собирает данные о процессоре в словарь
    """
    return {"cpu_load": cpu_percent(interval=1), "cpu_temp": _cpu_temp(),
            "cpu_freq": round(cpu_freq().current, -2)}
