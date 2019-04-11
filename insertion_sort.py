#!/usr/bin/env python
# -*- coding: utf-8 -*-

def insertion_sort(a):    
    for i in range(1, len(a)):
        if i == 1 and a[0] > a[i]:
            mem = a[0]
            a[0] = a[i]
            a[i] = mem
        elif a[i] > a[i-1]:
            continue
        elif a[i] < a[i-1]:
            for x in range(i, 0, -1):
                if a[x] < a[x-1] and x != 0:
                    mem = a[x-1]
                    a[x-1] = a[x]
                    a[x] = mem
                if a[x] >= a[x-2] and x !=0:
                    break