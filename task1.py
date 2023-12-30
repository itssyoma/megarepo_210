#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def geometric_mean(*a):
    if not a:
        return None
    n = len(a)
    count = 1
    for i in a:
        count *= i
    return count ** (1 / n)


if __name__ == "__main__":
    print(geometric_mean(4, 5, 8))
    print(geometric_mean())
