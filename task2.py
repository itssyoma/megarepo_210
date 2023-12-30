#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def average_harmonic(*a):
    if not a:
        return None
    count = 0
    for i in a:
        count += i ** -1
    return len(a) / count


if __name__ == "__main__":
    print(average_harmonic(1, 5, 7, 3))
    print(average_harmonic())
