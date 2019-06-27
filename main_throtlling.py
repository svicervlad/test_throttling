"""
Основной скрипт который запускает тесты и сохраняет графики
"""
from test import kernel_test, single_core_fibonacci
from grafic_test import grafic
from throttling import trottling


print("Start testing")
RESULT_FIBONACCI_TEST = single_core_fibonacci()
grafic(RESULT_FIBONACCI_TEST[1], "TEST_FIBONACCI")
trottling(RESULT_FIBONACCI_TEST[1], "TEST_FIBONACCI")

RESULT_KERNEL_TEST = kernel_test()
grafic(RESULT_KERNEL_TEST["get_kernel_test"][1], "TEST_GET_KERNEL")
grafic(RESULT_KERNEL_TEST["extract_kernel_test"][1], "TEST_EXTRACT_KERNEL")
grafic(RESULT_KERNEL_TEST["make_kernel_test"][1], "TEST_MAKE_KERNEL")
trottling(RESULT_KERNEL_TEST["get_kernel_test"][1], "TEST_GET_KERNEL")
trottling(RESULT_KERNEL_TEST["extract_kernel_test"][1], "TEST_EXTRACT_KERNEL")
trottling(RESULT_KERNEL_TEST["make_kernel_test"][1], "TEST_MAKE_KERNEL")

print("testing done")
