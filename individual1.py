#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


def product_between_min_max(*args):
    if args:
        start_index = min(args.index(min(args)), args.index(max(args))) + 1
        end_index = max(args.index(min(args)), args.index(max(args)))
        nums_for_product = [i for i in args[start_index:end_index]]
        return np.prod(nums_for_product)
    else:
        return None


if __name__ == "__main__":
    print("Произведение чисел между max и min =", product_between_min_max(1, 2, 3, 300, 5, 6, 7, -300, 14, 15, 16))
    print("Результат передачи пустого списка аргументов: ", product_between_min_max())
