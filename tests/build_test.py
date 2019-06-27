"""
Тест сборки ядра linux
"""
import os
import tarfile
from psutil import cpu_count

PATH = os.path.abspath(os.path.join(__file__, os.pardir))
CONFIG_FILE = os.path.join(PATH, "src/some_kernel_config")
BUILD_PATH = "/tmp/test_build"
ARCHIVE = "linux.tar.xz"
SRC = "linux-4.19.51"
SRC_PATH = os.path.join(BUILD_PATH, SRC)
ARCHIVE_PATH = os.path.join(BUILD_PATH, ARCHIVE)
URL = "https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.19.51.tar.xz"


def get_kernel():
    """
    загружает архив с исходником ядра
    """
    if not os.path.isdir(BUILD_PATH):
        os.mkdir(BUILD_PATH)
    if not os.path.isfile(ARCHIVE_PATH):
        out_wget = os.system(f"/usr/bin/wget {URL} -O {ARCHIVE_PATH}")
        if out_wget > 0:
            # wget возвращает >0 если какя-то ошибка, но создает файл в системе
            os.remove(ARCHIVE_PATH)
            raise SystemError(f"download error {out_wget}")
        print("get_kernel: done")
    else:
        raise FileExistsError(f"download error, file {ARCHIVE_PATH} exists")


def extract_kernel():
    """
    разархиврует архив с исходником ядра
    """
    if not os.path.isdir(BUILD_PATH) or not os.path.isfile(ARCHIVE_PATH):
        raise SystemError("not have build path or kernel archive ")
    print("extract kernel source")
    kernel_tar = tarfile.open(ARCHIVE_PATH)
    kernel_tar.extractall(path=BUILD_PATH)
    os.remove(ARCHIVE_PATH)
    print("extract_kernel: done")


def make_kernel():
    """
    собирает ядро, при ошибке останавливает выполнение программы.
    параметр сборки -j будет равен cpu_count+1
    """
    if not os.path.isdir(SRC_PATH):
        raise SystemError("error build kernel")
    os.system(f'cp {CONFIG_FILE} {os.path.join(SRC_PATH, ".config")}')
    os.chdir(SRC_PATH)
    os.system(f"make -j {cpu_count() + 1}")
    os.chdir(PATH)
    os.system(f'rm -rf {BUILD_PATH}')
    print("make_kernel: done")
