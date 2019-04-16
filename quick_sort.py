#!/usr/bin/env python
# -*- coding: utf-8 -*-

def quick_sort(massive, left=0, right=None):
    if right == None:
        right = len(massive) - 1
    if left >= right: 
        return
    
    left_m = left
    right_m = right
    fix = left
    while left <= right:
        while massive[left] < massive[fix]:
            left += 1
        while massive[right] > massive[fix]:
            right -= 1
        if left <= right:
            massive[left], massive[right] = massive[right], massive[left]
            left += 1
            right -= 1

    quick_sort(massive, left_m, right)
    quick_sort(massive, left, right_m)
    return massive