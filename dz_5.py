from functools import reduce


def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el


print(reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0]))