#!/usr/bin/env python
# -*- coding: utf-8 -*-

from timeit import default_timer as timer
from matplotlib import pyplot as plt
from tqdm import tqdm
from statistics import mean
import numpy as np

def selection_sort(a):
    min_val = a[0]
    min_num = 0
    mem_val = 0
    n = 0

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
                if a[x] < a[x-1] and i != 0:
                    mem = a[x-1]
                    a[x-1] = a[x]
                    a[x] = mem

def measure_search_time(sort_function, sz, repeats):
    """
    Возвращает результат замеров скорости выполнения сортировки
    """
    results = []
    for i in range(repeats):
        data = np.random.rand(sz)
        start = timer()
        sort_function(data)
        end = timer()
        results.append(end - start)
    return mean(results)


def main():
    algorithms = {
        'sorted': sorted,
        'selection_sort': lambda a: selection_sort(a),
        'insertion_sort': lambda a: insertion_sort(a),
        'np_quicksort': lambda a: np.sort(a, kind='quicksort'),
        'np_mergesort': lambda a: np.sort(a, kind='mergesort')
    }

    sizes = list(range(1, 100, 5)) + list(range(20, 500, 50))
    avg_time = {alg: [] for alg in algorithms}
    for sz in tqdm(sizes):
        for alg_name, f in algorithms.items():
            avg_time[alg_name].append(measure_search_time(f, sz, 100))

    for alg_name in algorithms:
        plt.plot(sizes, avg_time[alg_name], label=alg_name)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()