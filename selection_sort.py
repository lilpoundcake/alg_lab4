#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def selection_sort(a):
    min_val = a[0]
    min_num = 0
    mem_val = 0
    n = 0
    print(a)

    while n != len(a):
        min_val = a[n]
        min_num = n

        for i in range(n, len(a)):
            if a[i] < min_val:
                min_val = a[i]
                min_num = i
            else:
                continue

            mem_val = a[n]
            a[n] = min_val
            a[min_num] = mem_val
        n += 1


a = [random.randint(1, 100) for i in range(20)]
selection_sort(a)
print(a)